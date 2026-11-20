"""Two-process harmless-file observation demo; not hostile-host isolation."""
import hashlib
import hmac
import json
import multiprocessing as mp
from pathlib import Path
import secrets
import tempfile

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':')).encode('ascii')

def executor(path, payload):
    Path(path).write_bytes(payload)

def observer(path, run_id, action_id, key, pipe):
    try:
        data = Path(path).read_bytes()
        report = {'run_id': run_id, 'action_id': action_id,
                  'sha256': hashlib.sha256(data).hexdigest(), 'observed': True}
    except OSError:
        report = {'run_id': run_id, 'action_id': action_id,
                  'sha256': None, 'observed': False}
    tag = hmac.new(key, canonical(report), hashlib.sha256).hexdigest()
    pipe.send((report, tag))
    pipe.close()

def run_trial(payload=b'authorized harmless write', tamper=False, omit=False,
              prepopulate=False, inject_after_precheck=False):
    """Prestate check blocks preexisting targets; not race-safe attestation."""
    with tempfile.TemporaryDirectory() as directory:
        path = str(Path(directory) / (secrets.token_hex(16) + '.bin'))
        key = secrets.token_bytes(32)
        run_id, action_id = secrets.token_hex(8), 'write-1'
        if prepopulate:
            Path(path).write_bytes(payload)
        # Parent-controlled prestate check; same-host races remain possible.
        if Path(path).exists():
            return 'REJECT'
        # Adversarial negative-control hook: a separate actor can create the
        # expected bytes after the parent checks absence but before observation.
        if inject_after_precheck:
            Path(path).write_bytes(payload)
        if not omit:
            proc = mp.Process(target=executor, args=(path, payload))
            proc.start()
            proc.join(5)
            if proc.is_alive():
                proc.terminate()
                proc.join()
                return 'UNKNOWN'
            if proc.exitcode != 0:
                return 'UNKNOWN'
        if tamper and not omit:
            Path(path).write_bytes(b'substituted')
        parent, child = mp.Pipe(duplex=False)
        proc = mp.Process(target=observer, args=(path, run_id, action_id, key, child))
        proc.start()
        child.close()
        if not parent.poll(5):
            proc.terminate()
            proc.join()
            return 'UNKNOWN'
        report, tag = parent.recv()
        proc.join(5)
        if proc.exitcode != 0:
            return 'UNKNOWN'
        if not hmac.compare_digest(hmac.new(key, canonical(report), hashlib.sha256).hexdigest(), tag):
            return 'REJECT'
        if report['run_id'] != run_id or report['action_id'] != action_id:
            return 'REJECT'
        if not report['observed']:
            return 'UNKNOWN'
        return 'VERIFIED' if report['sha256'] == hashlib.sha256(payload).hexdigest() else 'REJECT'

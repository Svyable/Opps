"""SQLite-backed single-use envelope verification; NOT independent observation.

Requires a trusted SQLite file inaccessible to the untrusted agent. Successful
verification consumes the (run_id, action_id) pair, even if a later caller
cannot act on the result. SQLite's UNIQUE constraint arbitrates concurrent uses.
"""
import sqlite3
from recorder import verify


def initialize(connection):
    connection.execute('CREATE TABLE IF NOT EXISTS consumed_events ('
                       'run_id TEXT NOT NULL, action_id TEXT NOT NULL, '
                       'PRIMARY KEY (run_id, action_id))')
    connection.commit()


def verify_once(connection, event, tag, key, expected_run, expected_action,
                expected_path, expected_digest):
    result = verify(event, tag, key, expected_run, expected_action,
                    expected_path, expected_digest)
    if result != 'VERIFIED':
        return result
    # The transaction serializes writers across processes sharing one database.
    # A UNIQUE violation is a replay; other database errors must not be hidden.
    try:
        with connection:
            connection.execute('INSERT INTO consumed_events(run_id, action_id) '
                               'VALUES (?, ?)', (expected_run, expected_action))
    except sqlite3.IntegrityError:
        return 'REJECT'
    return 'VERIFIED'

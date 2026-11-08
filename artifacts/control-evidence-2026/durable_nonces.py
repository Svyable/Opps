"""Durable nonce-consumption gate for synthetic Control Evidence receipts.

SQLite UNIQUE constraint makes consume atomic across processes and restarts.
Store must reside on a persistent trusted local filesystem. This is NOT
independent recorder authentication or proof of complete coverage.
"""
import sqlite3


class SQLiteNonceRegistry:
    def __init__(self, path):
        if not path or path == ":memory:":
            raise ValueError("persistent SQLite path required")
        self.connection = sqlite3.connect(path, timeout=10, isolation_level=None)
        self.connection.execute("PRAGMA busy_timeout=10000")
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS consumed_nonces "
            "(nonce TEXT PRIMARY KEY NOT NULL, consumed_at TEXT NOT NULL "
            "DEFAULT CURRENT_TIMESTAMP)"
        )

    def consume(self, nonce):
        if not isinstance(nonce, str) or not nonce:
            return False
        try:
            cursor = self.connection.execute(
                "INSERT OR IGNORE INTO consumed_nonces(nonce) VALUES (?)", (nonce,)
            )
            return cursor.rowcount == 1
        except sqlite3.Error:
            return False

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

"""Customize SQL Alchemy Engine to simplify some things."""
from sqlalchemy import create_engine, text
from flask import current_app


class DB():
    """Wrap a SQL Alchemy Engine and add some custom methods."""

    def __init__(
        self,
        isolation_level=None
    ):
        """Initialize DB."""
        self.engine = create_engine(
            current_app.config.get('SQLALCHEMY_DATABASE_URI'),
            connect_args={'timeout': 10},
            pool_pre_ping=True,
            pool_recycle=1800,
            isolation_level=isolation_level
        )

        self.conn = self.engine.connect()

        self.logger = current_app.logger
        self.reconnects = 0

    def do(self, query, args=None, dml=True):
        """Execute a query. Return any results."""
        self.logger.debug(f"Executing query:\n{query}\nWith arguments:\n{args}")
        results = self.conn.execute(text(query), args)

        if dml:
            return results.rowcount

        return results

    def select(self, query, args=None):
        """Select and return data as a dict."""
        results = self.do(query, args, dml=False)
        return results.mappings().all()

    def select_one(self, query, args=None):
        """Select a single row and return data as a dict."""
        for row in self.select(query, args):
            return dict(row)

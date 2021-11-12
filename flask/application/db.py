"""Customize SQL Alchemy Engine to simplify some things."""
from sqlalchemy import create_engine
from flask import current_app


class DB():
    """Wrap a SQL Alchemy Engine and add some custom methods."""

    def __init__(
        self,
        auto_commit=False
    ):
        """Initialize DB."""
        self.engine = create_engine(
            current_app.config.get('SQLALCHEMY_DATABASE_URI'),
            connect_args={'timeout': 10},
            pool_pre_ping=True,
            pool_recycle=1800
        )

        self.auto_commit = auto_commit
        self.logger = current_app.logger
        self.reconnects = 0

    def commit(self):
        """Commit."""
        return self.engine.commit()

    def do(self, query, args=None, dml=True):
        """Execute a query. Return any results."""
        self.logger.debug(f"Executing query:\n{query}\nWith arguments:\n{args}")
        results = self.engine.execute(query, args=args)
        if self.auto_commit and dml:
            self.commit()

        return results

    def select(self, query, args=None):
        """Select and return data as a dict."""
        results = self.do(query, args, dml=False)
        return [dict(r) for r in results]

    def select_one(self, query, args=None):
        """Select a single row and return data as a dict."""
        results = self.do(query, args, dml=False)
        for row in results.all():
            return dict(row)

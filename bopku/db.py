"""Helper class to get a database engine and to get a session."""
from typing import cast

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, scoped_session
from sqlalchemy.orm.session import sessionmaker

from bopku.config import config

engine = create_engine(config.database_uri)
Base = declarative_base(bind=engine)


def get_session(connection=None) -> Session:
    """Get a new db session."""
    session = scoped_session(sessionmaker(bind=engine))
    return cast(Session, session)

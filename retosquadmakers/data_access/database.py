from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DataBaseEngine:
    def __init__(self, url_connection: str):
        self.engine = create_engine(url_connection)

    def init_db(self) -> None:
        Base.metadata.create_all(bind=self.engine)

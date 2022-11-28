import os
from functools import lru_cache
from typing import Final

import databases
from pydantic import BaseSettings

from data_access.database import DataBaseEngine


class SettingsEnviron(BaseSettings):
    DATABASE_URL: Final[str] = os.environ["DATABASE_URL"]
    TEST_DATABASE_URL: Final[str] = os.environ["TEST_DATABASE_URL"]
    TEST: Final[bool] = os.environ.get("TEST")


@lru_cache()
def get_settings():
    return SettingsEnviron()


database = DataBaseEngine(url_connection=get_settings().DATABASE_URL)
async_database = databases.Database(
    get_settings().TEST_DATABASE_URL if get_settings().TEST else get_settings().DATABASE_URL)

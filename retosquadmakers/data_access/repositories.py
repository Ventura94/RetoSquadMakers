from abc import ABC, abstractmethod
from datetime import datetime
from typing import Type, Literal

from httpx import AsyncClient
from sqlalchemy import select, insert, update, delete

from retosquadmakers.data_access.database import Base
from retosquadmakers.data_access.models import JokeModel
from retosquadmakers.settings import async_database


class BaseRepository:
    model: Type[Base] = NotImplementedError

    async def get(self, **kwargs):
        return await async_database.fetch_one(select(self.model).filter_by(is_delete=False, **kwargs))

    async def create(self, **kwargs) -> None:
        kwargs["create_at"] = datetime.now()
        kwargs["is_delete"] = False
        return await async_database.execute(insert(self.model), values=kwargs)

    async def update(self, by: str = "id", **kwargs):
        await async_database.execute(update(self.model).filter_by(**{by: kwargs[by]}).values(**kwargs))

    async def delete(self, by: str = "id", soft: bool = True, **kwargs) -> None:
        if soft:
            await self.update(by=by, is_delete=True, delete_at=datetime.now(), **kwargs)
        else:
            await async_database.execute(delete(self.model).filter_by(**{by: kwargs[by]}))


class JokeBaseAPIRepository(ABC):
    client: AsyncClient = NotImplementedError

    @abstractmethod
    async def get_random_joke(self) -> dict[Literal["joke"], str]:
        pass


class ChuckNorrisRepository(JokeBaseAPIRepository):

    def __init__(self):
        self.client = AsyncClient(base_url="https://api.chucknorris.io/jokes")

    async def get_random_joke(self):
        response = await self.client.get("random")
        return {"joke": response.json()["value"]}


class CanHazDadJokeRepository(JokeBaseAPIRepository):

    def __init__(self):
        self.client = AsyncClient(base_url="https://icanhazdadjoke.com", headers={"Accept": "application/json"})

    async def get_random_joke(self):
        response = await self.client.get("")
        return response.json()


class JokeRepository(BaseRepository):
    model = JokeModel

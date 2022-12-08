from datetime import datetime

import pytest
from httpx import AsyncClient
from sqlalchemy import select, insert

from retosquadmakers.data_access.models import JokeModel
from retosquadmakers.settings import async_database


@pytest.mark.anyio
async def test_get_joke_with_none_param(client: AsyncClient):
    response = await client.get("/v1/joke")
    assert response.json()["joke"]
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_joke_with_dad_param(client: AsyncClient):
    response = await client.get("/v1/joke", params={"provider": "Dad"})
    assert response.json()["joke"]
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_joke_with_chuck_param(client: AsyncClient):
    response = await client.get("/v1/joke", params={"provider": "Chuck"})
    assert response.json()["joke"]
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_joke_with_random_param(client: AsyncClient):
    response = await client.get("/v1/joke", params={"provider": "Random"})
    assert response.json()["joke"]
    assert response.status_code == 200


@pytest.mark.anyio
async def test_add_joke(client: AsyncClient):
    response = await client.post("/v1/joke", data={"joke": "This is a joke"})
    assert response.json()["joke"] == "This is a joke"
    assert response.status_code == 201
    assert await async_database.fetch_one(select(JokeModel.id, JokeModel.joke).filter_by(joke="This is a joke"))


@pytest.fixture
async def create_joke():
    return await async_database.execute(insert(JokeModel),
                                        values={"create_at": datetime.now(), "is_delete": False,
                                                "joke": "This is a joke"})


@pytest.mark.anyio
async def test_update_joke(client: AsyncClient, create_joke: int):
    response = await client.patch("/v1/joke", data={"number": create_joke, "new_joke": "This is update joke"})
    assert response.json() == {"id": create_joke, "joke": "This is update joke"}
    assert response.status_code == 201
    joke = await async_database.fetch_one(select(JokeModel.id, JokeModel.joke).where(JokeModel.id == create_joke))
    assert joke.joke == "This is update joke"


@pytest.mark.anyio
async def test_delete_joke(client: AsyncClient, create_joke: int):
    response = await client.delete("/v1/joke", params={"number": create_joke})
    assert response.json() == {"detail": "Joke has been removed"}
    assert response.status_code == 200
    joke = await async_database.fetch_one(select(JokeModel).where(JokeModel.id == create_joke))
    assert joke.is_delete

from fastapi import APIRouter, Query, Depends, Form, status

from enums import JokeProviderEnum
from schemas import JokeSchema, JokeDBSchema
from service import JokeService
from core.exceptions import NotFound

router = APIRouter(prefix="/joke", tags=["Jokes"])


@router.get("", response_model=JokeSchema)
async def get_joke(service: JokeService = Depends(), provider: JokeProviderEnum | None = Query(default=None)):
    return await service.get_joke(provider)


@router.post("", response_model=JokeDBSchema, status_code=status.HTTP_201_CREATED)
async def add_joke(service: JokeService = Depends(), joke: str = Form()):
    _id = await service.repositories.joke_database_repository.create(joke=joke)
    return {"id": _id, "joke": joke}


@router.patch("", response_model=JokeDBSchema, status_code=status.HTTP_201_CREATED)
async def update_joke(service: JokeService = Depends(), number: int = Form(), new_joke: str = Form()):
    if not await service.repositories.joke_database_repository.get(id=number):
        raise NotFound("Joke not found")
    await service.repositories.joke_database_repository.update(id=number, joke=new_joke)
    return {"id": number, "joke": new_joke}


@router.delete("")
async def delete_joke(service: JokeService = Depends(), number: int = Query()):
    if not await service.repositories.joke_database_repository.get(id=number):
        raise NotFound("Joke not found")
    await service.repositories.joke_database_repository.delete(id=number)
    return {"detail": "Joke has been removed"}

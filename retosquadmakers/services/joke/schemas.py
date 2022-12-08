from core.schemas import UJSONModel


class JokeSchema(UJSONModel):
    joke: str


class JokeDBSchema(UJSONModel):
    id: int
    joke: str

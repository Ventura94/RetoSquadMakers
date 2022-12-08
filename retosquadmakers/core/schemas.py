import ujson
from pydantic import BaseModel


class UJSONModel(BaseModel):
    class Config:
        orm_mode = True
        json_loads = ujson.loads
        json_dumps = ujson.dumps

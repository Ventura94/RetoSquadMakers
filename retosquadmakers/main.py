from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from starlette.middleware.cors import CORSMiddleware

from services import joke, maths
from settings import database, async_database

app = FastAPI(title="SquadMakers", default_response_class=UJSONResponse)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])


@app.on_event("startup")
async def startup():
    database.init_db()
    await async_database.connect()


@app.on_event("shutdown")
async def shutdown():
    await async_database.disconnect()


app.include_router(joke.router, prefix="/v1")
app.include_router(maths.router, prefix="/v1")

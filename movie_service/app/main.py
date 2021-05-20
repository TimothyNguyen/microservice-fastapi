#~/movie-service/app/main.py
from fastapi import FastAPI
from app.api.movies import movies
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI()
# FastAPI provides some event handlers which you can use to 
# connect to our database when the application starts and 
# disconnect when it shuts down.
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(movies)
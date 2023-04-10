from fastapi import FastAPI
from models.api_logs import metadata,posts
# from database import Database
import sqlalchemy
from config.database import sqlalchemy_engine,Database, database
from routes.routes import router as post_router


app = FastAPI()


# DATABASE_URL = "sqlite:///advertisement.db"
# database = Database(DATABASE_URL)
# sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)


@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(sqlalchemy_engine)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

metadata.create_all(sqlalchemy_engine)
app.include_router(post_router)
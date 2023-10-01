from fastapi import FastAPI

from routers import survey, admin
from sql.database import SessionLocal, engine
from sql import models
import os

os.remove("sql_app.db")


app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(survey.router)
app.include_router(admin.router)


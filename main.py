from fastapi import FastAPI

from api import users, sections, courses

from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastApiApp",
    description= "User Management Application",
    version="0.0.1",
    contact={
        "name": "Rashid Nawaz",
        "email": "rashidnawaz533@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)
app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)

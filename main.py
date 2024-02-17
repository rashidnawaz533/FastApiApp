from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from api import users, sections, courses
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

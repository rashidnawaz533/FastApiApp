from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str

    class Config:
        DATABASE_URL= "postgresql+psycopg2://postgres:Rashid0300@localhost/fastapiapp"


settings = Settings()
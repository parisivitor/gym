from typing import List

from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from decouple import config

user = config('DB_USER')
password = config('DB_PASSWORD')
host = config('DB_HOST')
dbname = config('DB_DATABASE')
port = config('DB_PORT')



class Settings(BaseSettings):
    DB_URL: str = f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{dbname}'
    DBBaseModel = declarative_base()
    # engine = create_engine(DB_URL, echo=True, pool_size=20, max_overflow=0, connect_args={'connect_timeout': 10})
    # DBBaseModel = declarative_base(engine)

    JWT_SECRET: str = 'mB1DMvH3N-JOPSiaaTHHcqONBNnhuI78b24W6G65eaw'
    """
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()

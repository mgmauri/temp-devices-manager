from pydantic import BaseSettings


class Settings(BaseSettings):
    DRIVERSCONFIGFILE: str
    OPERATIONCONFIGFILE: str


# FIXME env_ setting
_env = "./app/src/core/.env"
settings = Settings(_env)

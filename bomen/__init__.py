import os

import pydantic
from dotenv import load_dotenv

load_dotenv()

payload = {k.lower(): os.environ[k] for k in ["DB_USER", "DB_PWD", "DB_HOST", "DB_NAME"]}


class Config(pydantic.BaseModel):
    db_user: str
    db_pwd: str
    db_host: str
    db_name: str


config = Config(**payload)

from typing import Optional, List
import uuid, datetime

from pydantic import BaseModel


class PersonSchemasBase(BaseModel):
    uuid: Optional[uuid.UUID]
    cpf: str
    name: str
    lastname: str
    celphone: str

    class Config:
        orm_mode = True

class PersonSchemaCreate(PersonSchemasBase):
    password: str

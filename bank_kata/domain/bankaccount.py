import datetime
import uuid
from uuid import *
from pydantic import BaseModel, Field, EmailStr


class NotFound(Exception):
    pass


class BankAccount(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    firstname: str
    lastname: str
    balance: int
    openingDate: str
    accountNumber: str

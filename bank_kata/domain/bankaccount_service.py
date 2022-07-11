import bank_kata.domain.bankaccount_repository

from pydantic import BaseModel, Field, EmailStr


class NotFound(Exception):
    pass


class BankAccountService(BaseModel):

    def __init__(self, repository: bank_kata.domain.bankaccount_repository, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def open_account(cls, firstname: str, lastname: str, initialbalance: int):
        raise NotImplementedError(u'STEP: Given I don\'t have any account')

import pytest

from bank_kata.domain.bankaccount_service import BankAccountService
from bank_kata.domain.bankaccount_repository import BankAccountRepository
from bank_kata.domain.bankaccount import BankAccount


def test_open_account():
    """
    GIVEN I don't own a bank account
    WHEN I create one
    THEN I receive a new Bank Account with a Bank Number
    """
    repo: BankAccountRepository = BankAccountRepository()
    service: BankAccountService = BankAccountService(repository=repo)

    bankAccount: BankAccount = service.open_account(firstname="Alex"
                                                    , lastname="Cuva"
                                                    , initialbalance=200)
    assert bankAccount.accountNumber is not None


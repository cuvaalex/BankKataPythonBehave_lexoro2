import os
import sqlite3
from bank_kata.domain.bankaccount_repository import BankAccountRepository

import bank_kata.domain


class BankAccountRepositoryLite(BankAccountRepository):

    def open_account(self, account: bank_kata.domain.bankaccount):
        raise NotImplementedError("Implement connection to DB")


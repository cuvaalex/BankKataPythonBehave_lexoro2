from behave import *

from bank_kata.domain.bankaccount_repository import BankAccountRepository
from bank_kata.domain.bankaccount_service import BankAccountService
from bank_kata.infra.bank_repository_lite import BankAccountRepositoryLite


class BankAccountSteps:

    @staticmethod
    def before_scenario():
        repository: BankAccountRepository = BankAccountRepositoryLite()
        service: BankAccountService = BankAccountService(repository=repository)

    @given(u'I don\'t have any account')
    def step_impl(self):
        raise NotImplementedError(u'STEP: Given I don\'t have any account')

    @given(u'I have a firstname "{firstname}"')
    def step_impl(self, firstname: str):
        raise NotImplementedError(u'STEP: Given I have a firstname "Mary"')

    @given(u'I have a lastname "{lastname}"')
    def step_impl(self, lastname: str):
        raise NotImplementedError(u'STEP: Given I have a lastname "Jackson"')

    @given(u'the initial balance is {balance}')
    def step_impl(self, balance: int):
        raise NotImplementedError(u'STEP: Given the initial balance is 200')

    @when(
        u'I open a new account with accountNumber "{accountNumber}", accountId {accountId} and openingDate "{openingDate}"')
    def step_impl(self, accountNumber: str, accountId: str, openingDate: str):
        raise NotImplementedError(
            u'STEP: When I open a new account with accountNumber "GB41OMQP68570038161775", accountId 3456 and openingDate "2022-02-23T10:15:30"')

    @then(u'I get his accountNumber "{accountNumber}"')
    def step_impl(self, accountNumber: str):
        raise NotImplementedError(u'STEP: Then I get his accountNumber "GB41OMQP68570038161775"')

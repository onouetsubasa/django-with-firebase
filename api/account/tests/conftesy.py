import pytest
from pytest_factoryboy import register
from .factory import AccountFactory


register(AccountFactory)
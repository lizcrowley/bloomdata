'''module docstring'''
from bloomdata.wallet import Wallet
import pytest

'''The pytest.fixutre functions are meant to replace 
the commented out code'''
@pytest.fixture
def empty_wallet():
    return Wallet()

@pytest.fixture
def wallet_20():
    return Wallet(20)



def test_empty_wallet(empty_wallet):
    #empty_wallet = Wallet()
    assert empty_wallet.balance == 0


def test_wallet_20(wallet_20):
    #assert Wallet(20).balance == 20
    assert wallet_20.balance == 20


def test_wallet_20_spend_10(wallet_20):
    #wallet_20 = Wallet(20)
    assert wallet_20.spend_cash(10) == "Remaining balance: 10"
    assert wallet_20.balance == 10


def test_spend_all_cash(wallet_20):
    #wallet_20 = Wallet(20)
    assert wallet_20.spend_cash(20) == "Remaining balance: 0"



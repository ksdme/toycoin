"""
    @author ksdme
    @created 26 August 2017 IST
    struct handles the txn
"""
from time import time
from toycoin.utils import validate_wallet_address
from toycoin.exceptions import MalformedTransaction

class Txn(object):
    """
        models the transaction
        used thorughout
    """

    def __init__(self, frm=None, to=None, amount=None):
        
        # validate both addresses
        if not validate_wallet_address(frm):
            raise MalformedTransaction(
                MalformedTransaction.BAD_FRM_ADDRESS)

        if not validate_wallet_address(to):
            raise MalformedTransaction(
                MalformedTransaction.BAD_TO_ADDRESS)

        self._frm = frm
        self._to = to

        # validate amount
        if not amount is None:
            if self.validate_amount(float(amount)):
                self._amount = amount
            else:
                raise MalformedTransaction(
                    MalformedTransaction.BAD_AMOUNT)
        else:
            self._amount = None

        self._timestamp = time()

    def validate_amount(self, amount=None):
        if amount is None:
            amount = self._amount

        return isinstance(amount, float) and amount > 0

    def json(self):
        """
            transforms current transaction into
            json readable form
        """

        txn = {
            "time": self.timestamp,
            "from": self.frm,
            "to": self.to,
            "sign": self.sign
        }

    timestamp = property(lambda self: self._timestamp)
    amount = property(lambda self: self._amount)
    frm = property(lambda self: self._frm)
    to = property(lambda self: self._to)

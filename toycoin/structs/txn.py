"""
    @author ksdme
    @created 26 August 2017 IST
    struct handles the txn
"""
from time import time
from json import dumps

from toycoin.exceptions import MalformedTransaction
from toycoin.utils import validate_wallet_address, sign_txn

class Txn(object):
    """
        models the transaction
        used thorughout
    """

    @staticmethod
    def validate_amount(amount=None):
        """
            validates the amount,
            it should be a number and > 0
        """

        return isinstance(amount, float) and amount > 0

    def __init__(self, inp, outputs):
        assert isinstance(outputs, list)

        # validate both addresses
        if not validate_wallet_address(inp):
            raise MalformedTransaction(
                MalformedTransaction.BAD_INP_ADDRESS)

        # ensure we have atleast one output
        if len(outputs) == 0:
            raise MalformedTransaction(
                MalformedTransaction.NO_OUTPUT_ADDR)

        # verify output addr and the amount too
        # assume that the outputs are the order of
        # (address, amount) [tuple]
        for out_addr, out_amt in outputs:
            if not validate_wallet_address(out_addr[0]):
                raise MalformedTransaction(
                    MalformedTransaction.BAD_OUT_ADDRESS)

            if not Txn.validate_amount(float(out_amt)):
                raise MalformedTransaction(
                    MalformedTransaction.BAD_AMOUNT)

        self._input = inp
        self._outputs = outputs
        self._timestamp = time()
        self._signed_outputs = None

    def sign(self, priv_key):
        """
            give it a private key and
            it'll generate sign the ops
        """
        signed_outputs = []
        for out_addr, out_amt in self._outputs:

            out_txn = {
                "amt": out_amt,
                "to": out_addr
            }

            signed_outputs.append({
                "to": out_addr,
                "amt": out_amt,
                "sign": sign_txn(dumps(out_txn), priv_key)
            })

        self._signed_outputs = signed_outputs
        return dict(signed_outputs)

    def json(self):
        """
            transforms current transaction into
            json readable form
        """

        if self._signed_outputs is None:
            raise MalformedTransaction(
                MalformedTransaction.UNSIGNED)

        txn = {
            "ver": "0.0.1",
            "id": "toycoin",
            "at": self.timestamp,

            "in": self.inp,
            "out": self.signed_outputs
        }

        return dumps(txn)

    inp = property(lambda self: self._input)
    outputs = property(lambda self: self._outputs)
    timestamp = property(lambda self: self._timestamp)
    signed_outputs = property(lambda self: self._signed_outputs)

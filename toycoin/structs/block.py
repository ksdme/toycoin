"""
    @author ksdme
    @created 27 August 2017 IST
"""
from time import time
from json import dumps

from toycoin.conf import BlockConf
from toycoin.structs.txn import Txn
from toycoin.exceptions import MalformedBlock

class Block(object):
    """
        Simply represents a general block
        on a the toycoin blockchain
    """

    def __init__(self, txs=None, nonce=""):
        assert isinstance(nonce, str)

        self._timestamp = int(time())
        self._nonce = nonce
        self._txs = []

        self.set_txs(txs)

    def add_tx(self, txn):
        """
            adds a transaction to the current
            block
        """
        assert isinstance(txn, Txn)

        # ensure the block isn't overcrowded
        if len(self.txs) >= BlockConf.MAX_TXNS_IN_BLOCK:
            raise MalformedBlock("block txs overflow")

        self._txs.append(txn)

    def set_txs(self, txs):
        """
            used to append a group of transactions
            doesn't replace the current block
        """
        assert txs is None or isinstance(txs, list)

        if txs is None:
            return

        for txn in txs:
            self.add_tx(txn)

    def json(self):
        """
            transforms a blocks into
            json form
        """
        block = {
            "time": self.timestamp,
            "nonce": self.nonce,
            "txs": map(lambda txn: txn.json(), self.txs)
        }

        return dumps(block)

    def mineable(self):
        """
            to make the block ready for mining
            you can always returns a partial json
            string and the miner can replace the nonce in string
            and mine it, it sounds lliek and efficient process
        """
        nonce = self._nonce

        self._nonce = BlockConf.MINEABLE_NONCE_PLACEHOLDER
        rep = self.json()
        self._nonce = nonce

        return rep

    txs = property(lambda self: self._txs)
    nonce = property(lambda self: self._nonce)
    timestamp = property(lambda self: self._timestamp)

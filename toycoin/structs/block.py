"""
    @author ksdme
    @created 27 August 2017 IST
"""
from json import dumps
from hashlib import md5

from toycoin.conf import BlockConf
from toycoin.structs.txn import Txn
from toycoin.exceptions import MalformedBlock
from toycoin.utils import validate_block_hash, get_time_milli, sort_by_alpha

class Block(object):
    """
        Simply represents a general block
        on a the toycoin blockchain
    """

    @staticmethod
    def calculate_hash(partial_block):
        """
            calculates the hash
            of the partial block which is then
            added to convert it into a complete block
        """
        assert isinstance(partial_block, dict)
        return md5(dumps(partial_block)).hexdigest()

    def __init__(self, prev_hash=None, txs=None, nonce="", difficulty=None):
        assert isinstance(nonce, str)

        self._timestamp = get_time_milli()
        self._difficulty = None
        self._prev_hash = None
        self._nonce = nonce
        self._txs = []

        self.set_txs(txs)
        self.set_prev_hash(prev_hash)
        self.set_difficulty(difficulty)

    def add_tx(self, txn):
        """
            adds a transaction to the current
            block
        """
        assert isinstance(txn, Txn)

        # ensure the block isn't overcrowded
        if len(self.txs) >= BlockConf.MAX_TXNS_IN_BLOCK:
            raise MalformedBlock(MalformedBlock.TXS_OVERFLOW)

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

    def set_prev_hash(self, hesh):
        """
            simply sets the prev hash
            onto this block
        """
        if hesh is None or not validate_block_hash(hesh):
            raise MalformedBlock(MalformedBlock.BAD_PREV_HASH)

        self._prev_hash = hesh

    def set_difficulty(self, difficulty):
        """
            set the current difficulty the block
            was mined with, other clients verify it
        """
        assert isinstance(difficulty, float)

        # it should be > 0
        if difficulty <= 0:
            raise MalformedBlock(
                MalformedBlock.BAD_DIFFICULTY)

        self._difficulty = difficulty

    def json(self):
        """
            transforms a blocks into
            json form
        """
        assert self.prev_hash is not None

        block = {
            "at": self.timestamp,
            "nonce": self.nonce,
            "prev_hash": self.prev_hash,
            "difficulty": self.difficulty,
            "txs": map(lambda txn: txn.json(), self.txs)
        }

        block_hash = Block.calculate_hash(block)
        block["hash"] = block_hash

        # sort the payload by key alphabet, to maintain
        # consistency
        block = sort_by_alpha(block)

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
    prev_hash = property(lambda self: self._prev_hash)
    difficulty = property(lambda self: self._difficulty)

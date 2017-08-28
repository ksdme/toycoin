"""
    @author ksdme
    @created 28 August 2017 IST
    creates a blockchain and helps
    traverse it too, help quantilfy
    the balance
"""
from json import loads, dumps
from toycoin.conf import BlockChainConf

class BlockChain(object):
    """
    """

    @staticmethod
    def validate_blockchain(chain):
        """
            validates the blockchain
            it simply ensures that the payload
            has the true hash and they match with
            the previous hash
        """
        assert isinstance(chain, list)

        for hook in chain[::-1]:
            pass

    def __init__(self):
        pass

    def load(self, filename=None):
        """
            loads the blockchain from the file,
            doesn't resolve the missing chain
        """
        if filename is None:
            filename = BlockChainConf.DEFAULT_CHAIN_DUMP_FILENAME

        with open(filename, "r") as chain:
            chain = loads(chain)

            # verify the integrity of the chain
            # before simply assuming that it is
            # a valid one

    def flush(self, filename=None):
        """
            periodically after a couple of blocks
            flush it to the file, you can always download
            the rest of the missing piece of the chain on
            from the network
        """
        if filename is None:
            filename = BlockChainConf.DEFAULT_CHAIN_DUMP_FILENAME

        with open(filename, "w") as dump:
            dump.write(dumps(self.chain))

    chain = property(lambda self: self._chain)

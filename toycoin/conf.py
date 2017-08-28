"""
    @author ksdme
    @created 26 August 2017 IST
    just a bunch of global settings
"""
from toycoin.utils import enum

class BlockConf(enum):
    """
        an enum containing values
        of certain conf paramaters of blocks
    """

    MAX_TXNS_IN_BLOCK = 20
    MINEABLE_NONCE_PLACEHOLDER = "{NONCE}"

class WalletConf(enum):
    """
        handles conf stuff for the wallet,
        such as key sizes and stuff
    """

    # bits, 40 Bytes
    KEY_PAIR_SIZE = 360

    # file names
    WALLET_FILE_EXTENSION = ".wallet"
    PUBLIC_KEY_FILE_NAME = "wallet_pub.pem"
    PRIVATE_KEY_FILE_NAME = "wallet_priv.pem"

class BlockChainConf(enum):
    """
        handles blockchain's conf,
        don't confuse with the settings
    """

    DEFAULT_CHAIN_DUMP_FILENAME = "./toycoin-chain"

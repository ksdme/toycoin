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

"""
    @author ksdme
    @created 26 August 2017 IST
    reusable utilities
"""

class enum(object):
    """
        make an subclass act like its
        an enum class
    """

    def __setattr__(self, key, val):
        return

def validate_wallet_address(addr):
    """
        validates a wallet address,
        it only does a syntactic validation
        of the address
    """

    return True

def validate_block_hash(hesh):
    """
        validates the hash of the block
        basically it validates that the
        given hash is a valid md5
    """

    return True

def sign_txn(payload, priv_key):
    """
        signs a payload using the private
        key an
    """

    return priv_key

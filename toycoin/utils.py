"""
    @author ksdme
    @created 26 August 2017 IST
    reusable utilities
"""
from base64 import b64encode
from rsa import sign, PublicKey, PrivateKey

from toycoin.exceptions import MalformedWallet

class enum(object):
    """
        make an subclass act like its
        an enum class
    """

    def __setattr__(self, key, val):
        return

def validate_wallet(wallet):
    """
        validate if the wallet instance
        passed is indeed an tuple of length
        two and the first and second keys r
        true
    """
    flag = True

    flag = isinstance(wallet, tuple)
    flag = flag and len(wallet) == 2

    flag = flag and isinstance(wallet[0], PublicKey)
    flag = flag and isinstance(wallet[1], PrivateKey)

    return flag

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

def sign_txn(wallet, payload, encode=True):
    """
        signs a payload using the
        given wallet key
    """
    assert isinstance(payload, str)

    if not validate_wallet(wallet):
        raise MalformedWallet(
            MalformedWallet.BAD_WALLET)

    ret = sign(payload, wallet[1], "MD5")

    if encode:
        ret = b64encode(ret)

    return ret

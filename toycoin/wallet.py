"""
    @author ksdme
    @created 26 August 2017 IST
    the wallet module, abstracts the process
    to helps generate new wallet keys, sign txns,
    submit txn
"""
from StringIO import StringIO
from os.path import isdir, join
from zipfile import ZipFile, ZIP_STORED
from rsa import newkeys, PublicKey, PrivateKey

from toycoin.conf import WalletConf
from toycoin.exceptions import MalformedWallet
from toycoin.utils import validate_wallet, transform_pub_key_to_alpha

class Wallet(object):
    """
        the core wallet class,
        it provides a number of functions
        that help with trivial wallet stuf
    """

    @staticmethod
    def new_wallet(poolsize=1):
        """
            simply generates and returns a new
            rsa key pair, cause this is what it
            uses
        """
        return newkeys(WalletConf.KEY_PAIR_SIZE, poolsize=poolsize)

    @staticmethod
    def load_wallet(uri):
        """
            loads a wallet from a public key file
            and a private key file
        """
        assert not isdir(uri)

        with ZipFile(uri, "r") as walletfile:
            pub_key = (PublicKey.load_pkcs1(walletfile.read(
                WalletConf.PUBLIC_KEY_FILE_NAME)))

            priv_key = PrivateKey.load_pkcs1(walletfile.read(
                WalletConf.PRIVATE_KEY_FILE_NAME))

        return pub_key, priv_key

    @staticmethod
    def save_wallet(key_pair, save_to):
        """
            saves a given wallet key pair to
            a given directory, in pem format
        """
        if isdir(save_to):
            save_to = join(save_to, "toycoin")

        pub_key, priv_key = key_pair
        save_to = save_to+WalletConf.WALLET_FILE_EXTENSION
        with ZipFile(save_to, "w", ZIP_STORED) as walletfile:

            binary_data = StringIO(pub_key.save_pkcs1(format="PEM")).getvalue()
            walletfile.writestr(WalletConf.PUBLIC_KEY_FILE_NAME, binary_data)

            binary_data = StringIO(priv_key.save_pkcs1(format="PEM")).getvalue()
            walletfile.writestr(WalletConf.PRIVATE_KEY_FILE_NAME, binary_data)

    @staticmethod
    def get_public_key(wallet):
        """
            takes a wallet and generates your
            public alphanumeric key
        """
        if not validate_wallet(wallet):
            raise MalformedWallet(
                MalformedWallet.BAD_WALLET)

        pub_key = str(wallet[0].n)
        return transform_pub_key_to_alpha(pub_key)

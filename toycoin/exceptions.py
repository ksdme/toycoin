"""
    @author ksdme
    @created 26 August 2017 IST
    handles exceptions
"""

class MalformedBlock(Exception):
    """ malformed block exception """

    BAD_PREV_HASH = "bad prev hash"
    BAD_DIFFICULTY = "bad difficulty"
    TXS_OVERFLOW = "block txs overflow"

    def __init__(self, msg):
        super(MalformedBlock, self).__init__(msg)

class MalformedTransaction(Exception):
    """ represents an malformed transaction """

    BAD_INP_ADDRESS = "input address"
    BAD_OUT_ADDRESS = "output address"
    BAD_AMOUNT = "unacceptable amount"
    NO_OUTPUT_ADDR = "need atleast one output"
    UNSIGNED = "outputs are unsigned"

    def __init__(self, msg):
        super(MalformedTransaction, self).__init__(msg)

class MalformedWallet(Exception):
    """ represents an malformed wallet """

    BAD_WALLET = "malformed wallet"

    def __init__(self, msg):
        super(MalformedWallet, self).__init__(msg)

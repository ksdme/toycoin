"""
    @author ksdme
    @created 26 August 2017 IST
    handles exceptions
"""

class MalformedBlock(Exception):
    """ malformed block exception """

    def __init__(self, msg):
        super(MalformedBlock, self).__init__(msg)

class MalformedTransaction(Exception):
    """ represents an malformed transaction """

    BAD_TO_ADDRESS = "to address"
    BAD_FRM_ADDRESS = "from address"
    BAD_AMOUNT = "unacceptable amount"

    def __init__(self, msg):
        super(MalformedTransaction, self).__init__(msg)

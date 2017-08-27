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
    return True

BlockChain here is a simple python list which is checked for consistency everytime. It completely depends on the idea that
python lists are consistent with the ordering of the list element, also toycoin depends on the timestamp of the block creation
to resolve any conflicts directly and also periodically after every n blocks of validation failure tries to sync with the nw

TODOS:

1) nowhere in the txn validation system has been progammed to check for balances and whether op <= in, please remember to do that.

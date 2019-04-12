import os
import logging
import hashlib
from sawtooth_sdk.processor.exceptions import InvalidTransaction
import handler.addressing as Addressing
import assets_pb2 as assets
import json

current_dir=os.path.dirname(__file__)
LOGGER = logging.getLogger(__name__)

with open(os.path.join(current_dir, '../config.json')) as json_config:
    config = json.load(json_config)

"""
Checking whether signer is admin or not based on the public key
"""
# def check_admin_signer(signer):
#     if config["admin_signer_public_key"]!= signer:
#         return False
#     return True

# def check_user_type(signer,userType,context):
#     user_address=Addressing.get_user_address(signer)
#     user_entry=context.get_state([user_address])
#     LOGGER.debug(user_entry)
    


def store_Trail(userName,txId,txTimestamp,userAddress,status):
    """provide a serialized version of the provided arguments

    Keyword arguments:
    userName -- Customer Name |
    txId -- transaction ID |
    txTimestamp -- transaction timestamp |
    userAddress -- user's blockchain address committing this transaction |
    status -- status as per bank proto file |
       """
    thisTrail = assets.Trail()
    thisTrail.userName =userName
    thisTrail.txnNumber=txId
    thisTrail.timestamp=txTimestamp
    thisTrail.userAddress=userAddress
    thisTrail.action=status
    address = Addressing.get_trail_address(userName,userAddress,txId)
    thisTrail.address = address
    LOGGER.debug("here in function")
    serializedString = thisTrail.SerializeToString()
    return  [address,serializedString]

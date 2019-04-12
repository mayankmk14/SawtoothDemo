import logging
import hashlib

import assets_pb2 as assets
from sawtooth_sdk.processor.exceptions import InvalidTransaction
import handler.addressing as Addressing
import handler.utils as utils

LOGGER = logging.getLogger(__name__)
def registerUser(payloadobj,signer,context,txId):

    formDetails = payloadobj.createAccount
    LOGGER.debug("USER FOUND-")
    LOGGER.debug(formDetails)
    # is_admin=utils.check_admin_signer(signer)
    # if not is_admin:
    #     raise InvalidTransaction("User Not admin")

    write_sets={}
    new_account=assets.Account()
    LOGGER.debug("PUB KEY FOUND-")
    LOGGER.debug(signer)
    new_account.address= Addressing.get_user_address(signer)
    new_account.userName=formDetails.name
    new_account.email=formDetails.email
    new_account.publicKey=signer
    LOGGER.debug("Account-")
    LOGGER.debug(new_account)
    user_check=context.get_state([new_account.address])
    if len(user_check)!= 0:
        raise InvalidTransaction("User already created")
    
    trail = utils.store_Trail(new_account.userName,txId,payloadobj.issueTimestamp,new_account.address,assets.Trail.ACCOUNT_CREATED)
    LOGGER.debug("TRAIL")
    LOGGER.debug(trail[1])
    write_sets[trail[0]] = trail[1]
    write_sets[new_account.address]=new_account.SerializeToString()
    
    context.set_state(write_sets)
    
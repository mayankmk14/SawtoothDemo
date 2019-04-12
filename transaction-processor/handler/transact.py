import logging
import hashlib

import assets_pb2 as assets
from sawtooth_sdk.processor.exceptions import InvalidTransaction
import handler.addressing as Addressing
import handler.utils as utils

LOGGER = logging.getLogger(__name__)
def transact(payloadobj,signer,context,txId):

    formDetails = payloadobj.transact
    LOGGER.debug(formDetails)
    write_sets={}
    address = Addressing.get_user_address(signer)
    data_check=context.get_state([address])

    if len(data_check) == 0:
        raise InvalidTransaction("User Doesn't Exist In Distributed Ledger")        
    
    # if data_check[2].address == orderAddress:
    #     raise InvalidTransaction("Order Id has already created")
    #     LOGGER.debug("Reaching here 44")
   

    user=assets.Account()
    LOGGER.debug(signer)
    user.ParseFromString(data_check[0].data)
    LOGGER.debug(formDetails.type)
    
    if(formDetails.type == assets.Trail.CREDIT):
        LOGGER.debug("CREDITING")
        user.balance += formDetails.amount
    elif(formDetails.type == assets.Trail.DEBIT):
        if(user.balance < formDetails.amount):
            raise InvalidTransaction("Insufficient Balance..!")
        user.balance -= formDetails.amount
        LOGGER.debug("DEBITING")
    LOGGER.debug("balance")
    LOGGER.debug(user.balance)

    write_sets[address]=user.SerializeToString()
    context.set_state(write_sets)
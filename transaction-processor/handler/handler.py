import logging
import hashlib
from sawtooth_sdk.processor.handler import TransactionHandler
import transaction_pb2 as tx_payload
from sawtooth_sdk.processor.exceptions import InvalidTransaction
from sawtooth_sdk.processor.exceptions import InternalError
import handler.balance as Balance
import handler.registerUser as RegisterUser
import handler.transact as Transact
import json
import os

current_dir=os.path.dirname(__file__)

LOGGER = logging.getLogger(__name__)

NAMESPACE = 'Bank'
namespacePrefix = hashlib.sha512(NAMESPACE.encode('utf8')).hexdigest()[:6]

class BankingTransaction(TransactionHandler):
    @property
    def family_name(self):
        return 'Bank'

    @property
    def family_versions(self):
        return ['1.0']

    @property
    def namespaces(self):
        return [NAMESPACE]


    def apply(self, transaction, context):

            payloadobj=tx_payload.Payload()
            LOGGER.debug("TX ID-")
            LOGGER.error(transaction.signature)
            signer = transaction.header.signer_public_key
            LOGGER.debug("m in handlerrrr")
            LOGGER.debug(payloadobj.action)
            payloadobj.ParseFromString(transaction.payload)
            LOGGER.debug(signer)
            
            actionSwitcher= {
                tx_payload.Payload.ACCOUNT:RegisterUser.registerUser,
                tx_payload.Payload.TRANSACT:Transact.transact,
                tx_payload.Payload.BALANCE : Balance.checkBalance
                
            }

            if not (payloadobj.action in actionSwitcher):
                LOGGER.debug("no function invoked- "+payloadobj.action)
                raise InvalidTransaction("No action taken")

            LOGGER.debug('action'+str(payloadobj))
            command=actionSwitcher[payloadobj.action]
            try:
                command(payloadobj,signer,context,transaction.signature)
                LOGGER.debug("Done with function")
            except Exception as ex:
                logging.exception('Caught an error',ex)



   
    # def apply(self, transaction, context):
    #     header = transaction.header
    #     load = Load(transaction.payload)
    #     assist = bank_pb2.Payload()
    #     print(load)
    #     if(not load.action in [0, 1, 2]):
    #         raise InvalidTransaction('Invalid action')
    #     address = self.createAddress(load.name)
    #     #Logger.debug("Atankwadi...!")
    #     account = self.get_state_data(address, context)
    #     if(load.action == 0):
    #         if(account):
    #             raise InvalidTransaction('Need Multiple Bank Account...U ain\'t getting Another')
    #         account = bank_pb2.Payload()
    #         account.name = load.name
    #         account.bal = load.bal
    #         data = account.SerializeToString()
    #         self.set_state_data(address, data, context)
    #         print('Account Created')
    #     elif(load.action == 1):
    #         if(account):
    #             if(load.type == 'D'):
    #                 if(load.amount <= account.bal):
    #                     account.bal -= load.amount
    #                     data = account.SerializeToString()
    #                     self.set_state_data(address, data, context)
    #                     print(account.bal)
    #                 else:
    #                     print('Sorry...But your account balance is low : ' + str(account.bal))
    #             elif(load.type == 'C'):
    #                 account.bal += load.amount
    #                 data = account.SerializeToString()
    #                 self.set_state_data(address, data, context)
    #                 print(account.bal)
    #         else:
    #             print('You Need an Account First...!')
    #     elif(load.action == 2):
    #         if(account):
    #             print(account.bal)
    #         else:
    #             print('Account Does Not Exist Moron...!')

    # def get_state_data(self, address, context):
    #     state_entries = context.get_state([address])
    #     acc = bank_pb2.Payload()

    #     try:
    #         acc.ParseFromString(state_entries[0].data)

    #     except IndexError:
    #         return {}
    #     except:
    #         raise InvalidTransaction('Failed to get State Data')
    #     return acc

    # def set_state_data(self, address, data, context):
    #     address = context.set_state({address: data})
    #     if(not address):
    #         raise InternalError('State Set Error')

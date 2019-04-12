import hashlib
import json
import os
from sawtooth_sdk.processor.exceptions import InvalidTransaction
import handler.constants as Constants
import assets_pb2 as assets

current_dir=os.path.dirname(__file__)

with open(os.path.join(current_dir, '../config.json')) as json_config:
    config = json.load(json_config)

TF_ADDRESS_PREFIX = hashlib.sha512(config["FAMILY_NAME"].encode('utf-8')).hexdigest()[0:6]


"""
assetPrefix for assets which are created per user
sharedPrefix for events which invlove assets that are shared or might transfer from one user to another.
"""
assetPrefix={
    Constants.ASSET_TYPE_USER : hashlib.sha512(Constants.ASSET_TYPE_USER.encode('utf-8')).hexdigest()[0:6],
    Constants.ASSET_TYPE_TRAIL : hashlib.sha512(Constants.ASSET_TYPE_TRAIL.encode('utf-8')).hexdigest()[0:6]
    
}


constantPrefix = hashlib.sha512('bank'.encode('utf-8')).hexdigest()[0:6]

"""
get_user_address- creates the user's account storage address
addressing scheme- | family prefix namespace(6 characters)    |   +    | asset type namespace(6 characters)   |   +   | user namespace(10 characters)  |
                   |          sha512(familyfamily_name)[0:6]  |        |        sha512(asset_type)[0:6]       |       |          signer[0:58]          |
"""

def get_user_address(signer):
    return TF_ADDRESS_PREFIX + assetPrefix[Constants.ASSET_TYPE_USER]+ signer[0:58]


# def get_bulk_asset_addresses(assetType,signer,asset_ids):
#     if not(assetType in assetPrefix):
#         raise InvalidTransaction("Wrong type of asset")

#     result_addresses=[]
#     for asset_id in asset_ids:
#         result_addresses.append(TF_ADDRESS_PREFIX + signer[0:10] + assetPrefix[assetType]  +  hashlib.sha512(asset_id.encode('utf-8')).hexdigest()[0:48])

#     return result_addresses




def get_trail_address(userName,userAddress,txId):
    return TF_ADDRESS_PREFIX + assetPrefix[Constants.ASSET_TYPE_TRAIL] + hashlib.sha512(userName.encode('utf-8')).hexdigest()[0:34] +  hashlib.sha512(userAddress.encode('utf-8')).hexdigest()[0:12] +  hashlib.sha512(txId.encode('utf-8')).hexdigest()[0:12]

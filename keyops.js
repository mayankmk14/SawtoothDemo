const {createContext, CryptoFactory} = require('sawtooth-sdk/signing')
const context = createContext('secp256k1')
const config=require('./config.json')
const path=require('path');
const fs=require('fs-extra')
var protoObj = require("protobufjs");
const {createHash} = require('crypto')
const {protobuf} = require('sawtooth-sdk')

fs.ensureDirSync(path.join(__dirname,'./',config.keystore))


/**
 * Generate a sawtooth private key
 * @return hex encoded private key
 */

function generatePrivateKey() {

    const privateKey = context.newRandomPrivateKey();
    var hexEncoded=privateKey.asHex();
    return {privateKey,hexEncoded}
}


/**
 * parsing private key to create buffer
 * @param {string} hexEncoded hex encoded private key
 * @return Buffer of private key
 */

function parsePrivateKey(hexEncoded) {

    var decodedPriv=Buffer.from(hexEncoded,'hex')
    var privateBuffer = {
        privateKeyBytes: decodedPriv
    }
    return privateBuffer;
}


/**
 * Create a sawtooth private key
 * @return hex encoded private key
 */

function createPrivateKeyForUser(username){

    var filepath=path.join(__dirname,'./',config.keystore,username+'.pem');
    if (fs.existsSync(filepath)){
        throw('Private key for the user already exists!');
    }
    var keyObj=generatePrivateKey();
    
    return fs.writeFileSync(filepath,keyObj.hexEncoded);
}

/**
 * Get a sawtooth private key
 * @return hex encoded private key
 */




function getPrivateKey(username){
    var filepath=path.join(__dirname,'./',config.keystore,username+'.pem');
    if (!fs.existsSync(filepath)){
        throw("Private key for the user doesn't exist!");
        
    }
    return fs.readFileSync(filepath).toString()

}


/**
 * Create signer object for private key
 * @param {string} privateKey Private key
 * @return Signer object
 */
function getSigner(username) {

    var hexEncodedPrivatekey=getPrivateKey(username);
    var privateKeyBuffer=parsePrivateKey(hexEncodedPrivatekey)
    var signer=new CryptoFactory(context).newSigner(privateKeyBuffer)
    return new CryptoFactory(context).newSigner(privateKeyBuffer)

}


/**
 * get public key
 * @param {string} privateKey hex encoded private key
 * @return signer
 */

 function getUserPublicKey(username) {
    console.log("get the user public key")
    var privateKey= getPrivateKey(username);
    console.log("private Key" ,privateKey)
    var signer =new CryptoFactory(context).newSigner(privateKey)
    console.info("Signer ",signer)
    var hexPriv=privateKey;
    var decodedPriv=Buffer.from(hexPriv,'hex')
      var privateBuffer = {
     privateKeyBytes: decodedPriv
   }
   console.log("after decoding hexadecimal- ",privateBuffer)
 
  signer = new CryptoFactory(context).newSigner(privateBuffer).getPublicKey().asHex();

 console.log("Public key",signer)

   return signer;
}

exports.getSigner=getSigner;
exports.createPrivateKeyForUser=createPrivateKeyForUser;
exports.parsePrivateKey=parsePrivateKey;
exports.getUserPublicKey=getUserPublicKey;
exports.getPrivateKey=getPrivateKey;


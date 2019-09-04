//Creating private key
const {
    createContext,
    CryptoFactory
} = require('sawtooth-sdk/signing')
const crypto = require('crypto');
const context = createContext('secp256k1')
var readlineSync = require('readline-sync');
const keyOps = require('./keyops.js')
const config = require('./config.json')
var protoObj = require("protobufjs");
const request = require('request')
const restapiURL = 'http://localhost:8008'
const asset = require('./proto/compiled_proto/assets')

//Encoding of Payload

protoObj.load('./proto/transaction.proto', function (err, root) {
    if (err)
        throw err;

    console.log("ROOT_")

    var tx = root.lookupType("SawDemo.Payload");



    option = readlineSync.question('options?' + "\n" + '1. Create Private key' + "\n" + '2. Doing Transaction' + "\n" + 'Enter your choices' + "\n");

    if (option == '1') {
        // Creating private key
        console.log("Generating Private Key")
        username = readlineSync.question('Enter a username :');
        PrivateKey = keyOps.createPrivateKeyForUser(username); //user Private Key
        userPublicKey = keyOps.getUserPublicKey(username); //user Public Key
        console.log("Private key", PrivateKey);
        console.log("Public key", userPublicKey);
        console.log("Restart the file to now do a transaction...\nPrivate key is saved in Keys Directory and is auto accessed for signing Transactions")
        return;
    } else if (option == '2') {
        // doing transaction
        console.log("Proceed to transaction");
        username = readlineSync.question('username : ');
        PrivateKey = keyOps.getPrivateKey(username); //user Private Key
        userPublicKey = keyOps.getUserPublicKey(username); //user Public Key
        choice = readlineSync.question('operations choice?' + "\n" + '1. Create Account' + "\n" + '2. Credit' + "\n" + '3. Debit' + "\n" + '4. Balance \n');
        if (choice == 1) {
            // payload for ACCOUNT CREATION operation
            var email = readlineSync.question("Enter your Email : ")
            var payload = {
                action: tx.Action.ACCOUNT,
                createAccount: {
                    name: username,
                    email: email
                },
                submissionTimestamp: "" + new Date().getTime()
            }

        } else if (choice == 2) {
            // payload for CREDIT operation
            var amount = readlineSync.questionFloat("Enter Amount for Transaction : ")
            var payload = {
                action: tx.Action.TRANSACT,
                transact: {
                    type: tx.Transact.Type.CREDIT,
                    amount: amount
                },
                submissionTimestamp: "" + new Date().getTime()
            }


        } else if (choice == 3) {
            // payload for DEBIT operation
            var amount = readlineSync.questionFloat("Enter Amount for Transaction : ")
            var payload = {
                action: tx.Action.TRANSACT,
                transact: {
                    type: tx.Transact.Type.DEBIT,
                    amount: amount
                },
                submissionTimestamp: new Date().getTime()
            }
        } else if (choice == 4) {

            let address = get_user_address(userPublicKey)
            getResult(address).then(data => {
                console.log("Your Balance is ----> ", data.balance)
            })
            return;
        } else {
            console.log("option is not available...BYE")
            return
        }
    } else {
        console.log("option is not available...BYE")
        return
    }


    privateBuffer = keyOps.parsePrivateKey(PrivateKey)
    console.log("after decoding hexadecimal- ", privateBuffer)

    var signer = new CryptoFactory(context).newSigner(privateBuffer);
    console.log("Signer-", signer);
    console.log("Public key", signer.getPublicKey().asHex())

    // .................................demoPayloads-not to be used..............................................

    // const payload = {
    //     action: tx.Action.CREATE_ORDER,
    //     createOrderPayload: {
    //         certificates:[{
    //                 issueTimestamp:"6516549845112",
    //                 documentHash:"1254fise9wi0943123i69545",
    //                 result :tx.ArgumentCertificate.Result.TESTING_PASSED_RECIEPT_ISSUED
    //             },
    //             {
    //                 issueTimestamp:"6516549845112",
    //                 documentHash:"12fi454se9wi0943isv123d65584695",
    //                 result :tx.ArgumentCertificate.Result.TESTING_FAILED_RECIEPT_ISSUED
    //             }],
    //     orderType:tx.CreateOrder.OrderTypeEnum.PGDC
    // }
    // }


    // ......console............console............console......console....................................console........



    var errMsg = tx.verify(payload);
    if (errMsg)
        throw Error(errMsg);

    // Create a new message
    var message = tx.create(payload); // or use .fromObject if conversion is necessary
    console.log("M-", message)
    // Encode a message to an Uint8Array (browser) or Buffer (node)
    var buffer = tx.encode(message).finish();
    console.log("BUFFER- ", buffer)

    var message = tx.decode(buffer);
    // ... do something with message
    console.log("DECODED MESSAGE- ", message)
    // If the application uses length-delimited buffers, there is also encodeDelimited and decodeDelimited.

    // Maybe convert the message back to a plain object
    var object = tx.toObject(message, {
        longs: String,
        enums: String,
        bytes: String,
        // see ConversionOptions
    });
    console.log("Object- ", object)

    const payloadBytes = buffer;
    console.log("payload Bytes-", payloadBytes)



    const {
        createHash
    } = require('crypto')
    const {
        protobuf
    } = require('sawtooth-sdk')

    const transactionHeaderBytes = protobuf.TransactionHeader.encode({
        batcherPublicKey: signer.getPublicKey().asHex(),
        dependencies: [],
        familyName: config.familyName,
        familyVersion: config.familyVersion,
        inputs: ['85b4aa'], //familyname i.e. opening of each addressing
        nonce: getNonce(),
        outputs: ['85b4aa'],
        payloadSha512: createHash('sha512').update(payloadBytes).digest('hex'),
        signerPublicKey: signer.getPublicKey().asHex()
        // In this example, we're signing the batch with the same private key,
        // but the batch can be signed by another party, in which case, the
        // public key will need to be associated with that key.
    }).finish()

    console.log("Transaction header- ", transactionHeaderBytes)



    const signature = signer.sign(transactionHeaderBytes)

    const transaction = protobuf.Transaction.create({
        header: transactionHeaderBytes,
        headerSignature: signature,
        payload: payloadBytes
    })


    console.log("Transaction- ", transaction);

    const transactions = [transaction]

    const batchHeaderBytes = protobuf.BatchHeader.encode({
        signerPublicKey: signer.getPublicKey().asHex(),
        transactionIds: transactions.map((txn) => txn.headerSignature),
    }).finish()

    console.log("batch header bytes- ", batchHeaderBytes);


    const batchSignature = signer.sign(batchHeaderBytes)

    const batch = protobuf.Batch.create({
        header: batchHeaderBytes,
        headerSignature: batchSignature,
        transactions: transactions,
        trace: true

    });

    const batchListBytes = protobuf.BatchList.encode({
        batches: [batch]
    }).finish()

    console.log("BatchListAsbytes- ", batchListBytes)

    request.post({
        url: config.restapiURL + '/batches',
        body: batchListBytes,
        headers: {
            'Content-Type': 'application/octet-stream'
        }
    }, (err, response) => {
        if (err) return console.log(err)
        console.log(response.body)
    })



});

function getResult(address) {
    return new Promise((resolve, reject) => {
        console.log("ADDRESS", address)
        request.get({
            url: restapiURL + '/state/' + address
        }, (err, response) => {
            if (err) {
                console.log("error in getResult", err)
                reject(err)
            }
            // decoded = base64.b64decode("")
            var bytes = new Buffer(JSON.parse(response.body).data, "base64")
            // var data = JSON.parse(response.body);
            let Account = asset.Account.decode(bytes)
            resolve({
                success: true,
                balance: Account.balance
            })
        })

    })
}


function get_user_address(publicKey) {
    let address = crypto.createHash('sha512').update(config.familyName).digest('hex').substring(0, 6) + crypto.createHash('sha512').update("asset_type_user").digest('hex').substring(0, 6) + publicKey.substring(0, 58)
    return address;
}



function getNonce() {
    var dateString = Date.now().toString(36).slice(-5);
    var randomString = Math.floor(Math.random() * 46655).toString(36);
    return dateString + ('00' + randomString).slice(-3);
}
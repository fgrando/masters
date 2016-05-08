#!/usr/bin/python

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter # for CTR

BLOCK_SIZE=16

print "CBC - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "

def pad(text):
    #chech if the string needs to be padded
    #since the text is an hex string, each 2 chars represent a byte, and the length of string will always be even
    tab = '\t'
    l = len(text)/2
    rem = l%BLOCK_SIZE
    if rem == 0:
        return text

    padByte = (BLOCK_SIZE - rem)  # divided by two because every 2 chars mean 1 byte in this hex string
    print tab + "is {} bytes long, needs padding of {} bytes".format(l, padByte)
    for i in range(0, padByte):
        text = text + hex(padByte)[2:].zfill(2)
    print tab + text
    print tab + "byte length after padding:", len(text)/2
    return text

def CBCdecrypt(ciphertext, key):
    IV = ciphertext[:BLOCK_SIZE] #previous 16 chars are out IV
    aes = AES.new(key, AES.MODE_CBC, IV)
    return aes.decrypt(ciphertext[BLOCK_SIZE:]) #discard IV in decryption process
def CBCencrypt(plaintext, key):
    # initialization vector
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(key, AES.MODE_CBC, IV)
    return IV.encode('hex') + aes.encrypt(plaintext).encode('hex')

CBCinputs= [
["", "140b41b22a29beb4061bda66b6747e14", "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"],
["", "140b41b22a29beb4061bda66b6747e14", "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"],
["4e657874205468757273646179206f6e65206f66207468652062657374207465616d7320696e2074686520776f726c642077696c6c2066616365206120626967206368616c6c656e676520696e20746865204c696265727461646f72657320646120416d6572696361204368616d70696f6e736869702e", "140b41b22a29beb4061bda66b6747e14", ""],
["", "140b41b22a29beb4061bda66b6747e14", "821128dded29daaea3f267c18e4b5a0285d0658f459a528d0b77f75bd4abdc36cb7bdacc8ab95d8b334e4411a546d995c01a6ac318fa48b8e00983fab1970ae28a618b7c1d82713fc82e4a470e287cc16ab2699dba4e8a6d80ff8d8e72ce64b0dca6d3cf360d0ce91716bdf8dd2873c53a1d92db2894138ae4337723021529942a7b83286f4e8fa34fe19c0b9e4841d7"]
]
for i in CBCinputs:
    #if lenght is not 3, the input is invalid
    if len(i) != 3:
        print "skipping invalid input..."
        continue

    print "input {}: ".format(CBCinputs.index(i))

    #the input is hex encoded
    plaintext =  pad(i[0])
    key =        pad(i[1])
    ciphertext = pad(i[2])

    # if has no plaintext, decode
    if plaintext == "":
        print ciphertext
        print CBCdecrypt(ciphertext.decode('hex'), key.decode('hex'))
    else:
        print plaintext.decode('hex')
        print CBCencrypt(plaintext.decode('hex'), key.decode('hex'))


print "\n\nCTR - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
def CTRdecrypt(ciphertext, key):
    IV = ciphertext[:16]
#    ctr = Counter.new(64, initial_value=long(IV, 16)) #64 bits long counter
    ctr = Counter.new(128, initial_value=long(IV.encode("hex"), 16)) #64 bits long counter initialized with IV
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.decrypt(ciphertext[16:])

def CTRencrypt(plaintext, key):
    IV = Random.new().read(BLOCK_SIZE)
    ctr = Counter.new(128, initial_value=long(IV.encode("hex"), 16)) #64 bits long counter, using some IV as prefix
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return IV.encode('hex') + aes.encrypt(plaintext).encode('hex')

#inputs is a list with [plaintext, key, ciphertext]
CTRinputs= [
["", "36f18357be4dbd77f050515c73fcf9f2", "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"],
["", "36f18357be4dbd77f050515c73fcf9f2", "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"],
["5468697320697320612073656e74656e636520746f20626520656e63727970746564207573696e672041455320616e6420435452206d6f64652e", "36f18357be4dbd77f050515c73fcf9f2", ""],
]
for i in CTRinputs:
    #if lenght is not 3, the input is invalid
    if len(i) != 3:
        print "skipping invalid input..."
        continue

    print "input {}: ".format(CTRinputs.index(i))

    #the input is hex encoded
    plaintext =  i[0]
    key =        i[1]
    ciphertext = i[2]

    # if has no plaintext, decode
    if plaintext == "":
        print ciphertext
        print CTRdecrypt(ciphertext.decode('hex'), key.decode('hex'))
    else:
        print plaintext.decode('hex')
        print CTRencrypt(plaintext.decode('hex'), key.decode('hex'))





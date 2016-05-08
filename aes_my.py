#!/usr/bin/python

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter # for CTR

BLOCK_SIZE=16

print "CBC - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "

def split_every(n, s):
    return [ s[i:i+n] for i in xrange(0, len(s), n) ]

def XOR(a, b):
    xor = ""
    for i in range(len(a)):
        xor = xor + hex(int(a[i], 16) ^ int(b[i], 16))[2:]
    return xor

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

def unpad(hexstr):
    return hexstr
    cipher = hexstr.encode('hex')
    bytes = split_every(2, cipher)
    print bytes
    last = hex(bytes[-1])
    if last > 0xf:
        return hexstr

    return hexstr
    

def CBCdecrypt(ciphertext, key):
    ciphertext = unpad(ciphertext)
    IV = ciphertext[:BLOCK_SIZE] #previous 16 chars are out IV
    
    plain = ""
    secret = ciphertext[BLOCK_SIZE:]
    if len(secret)%BLOCK_SIZE != 0:
        print "bad padding"
        exit(-1)

    blocks = split_every(BLOCK_SIZE, secret)
    blocks.reverse()
    # remove padding after decryption of first block
    for i in range(len(blocks)-1):
        aes = AES.new(key, AES.MODE_ECB)
        dec = aes.decrypt(blocks[i])
        xor = XOR(dec.encode('hex'), blocks[i+1].encode('hex')).decode('hex')
        plain = xor + plain

    last = blocks[-1]
    aes = AES.new(key, AES.MODE_ECB)
    dec = aes.decrypt(last)
    xor = XOR(dec.encode('hex'), IV.encode('hex')).decode('hex')
    plain = xor + plain
    return plain

def CBCencrypt(plaintext, key):
    IV = Random.new().read(BLOCK_SIZE)
    ciphertext = ""
    ciphertext = IV.encode('hex')
    blocks = split_every(BLOCK_SIZE, plaintext)
    for i in range(len(blocks)):
        xor = XOR(IV.encode('hex'), blocks[i].encode('hex')).decode('hex') # encode to hex to do xor, then decode back
        aes = AES.new(key, AES.MODE_ECB)
        enc = aes.encrypt(xor)
        ciphertext = ciphertext + enc.encode('hex')
        IV = enc
    return ciphertext


def CTRdecrypt(ciphertext, key):
    IV = ciphertext[:16]
#    ctr = Counter.new(64, initial_value=long(IV, 16)) #64 bits long counter
    ctr = Counter.new(128, initial_value=long(IV.encode("hex"), 16)) #64 bits long counter initialized with IV
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.decrypt(ciphertext[16:])

def CTRencrypt(plaintext, key):
    IV = Random.new().read(BLOCK_SIZE)
    ciphertext = ""
    ciphertext = IV.encode('hex')
    initial_value=long(IV.encode("hex"), 16))
    blocks = split_every(BLOCK_SIZE, plaintext)
    for block in blocks:
        aes = AES.new(key, AES.MODE_ECB)
        enc = aes.encrypt(counter)
        xor = XOR(enc.encode('hex'), blocks[i].encode('hex')).decode('hex') # encode to hex to do xor, then decode back
        ciphertext = ciphertext + xor.encode('hex')
        
    return ciphertext


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



#!/usr/bin/python

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter # for CTR

BLOCK_SIZE=16

def CBCdecrypt(ciphertext, key):
    IV = ciphertext[:BLOCK_SIZE] #previous 16 chars are out IV
    aes = AES.new(key, AES.MODE_CBC, IV)
    return aes.decrypt(ciphertext[BLOCK_SIZE:]) #discard IV in decryption process
def CBCencrypt(plaintext, key):
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(key, AES.MODE_CBC, IV)
    return IV.encode('hex') + aes.encrypt(plaintext).encode('hex')

def CTRdecrypt(ciphertext, key):
    IV = ciphertext[:BLOCK_SIZE]
    ctr = Counter.new(128, initial_value=long(IV.encode("hex"), 16)) #128 bits long counter initialized with IV
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.decrypt(ciphertext[BLOCK_SIZE:])

def CTRencrypt(plaintext, key):
    IV = Random.new().read(BLOCK_SIZE)
    ctr = Counter.new(128, initial_value=long(IV.encode("hex"), 16)) #128 bits long counter, using some IV as prefix
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return IV.encode('hex') + aes.encrypt(plaintext).encode('hex')

def pad(text):
    #chech if the string needs to be padded
    #since the text is an hex string, each 2 chars represent a byte, and the length of string will always be even
    tab = '\t'
    l = len(text)/2
    rem = l%BLOCK_SIZE
    if rem == 0:
        return text

    padByte = (BLOCK_SIZE - rem)  # divided by two because every 2 chars mean 1 byte in this hex string
    #print tab + "is {} bytes long, needs padding of {} bytes".format(l, padByte)
    for i in range(0, padByte):
        text = text + hex(padByte)[2:].zfill(2)
    #print tab + text
    #print tab + "byte length after padding:", len(text)/2
    return text

#XXX TODO: fix unpad
def unpad(hexstr):
    return hexstr
    cipher = hexstr.encode('hex')
    bytes = split_every(2, cipher)
    print bytes
    last = hex(bytes[-1])
    if last > 0xf:
        return hexstr
    return hexstr

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Local CTR and CBC encryption implementation
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def split_every(n, s):
    '''Split string s every n characters'''
    return [ s[i:i+n] for i in xrange(0, len(s), n) ]

def XOR(a, b):
    '''The XOR operation between a and b, that should be hex strings'''
    xor = ""
    for i in range(len(a)):
        xor = xor + hex(int(a[i], 16) ^ int(b[i], 16))[2:]
    return xor

def MyCBCdecrypt(ciphertext, key):
    '''Local CBC decryption implementation'''
    ciphertext = unpad(ciphertext)
    IV = ciphertext[:BLOCK_SIZE] #previous 16 chars are our IV
    
    plain = ""
    secret = ciphertext[BLOCK_SIZE:]
    if len(secret)%BLOCK_SIZE != 0:
        print "bad padding"
        exit(-1)

    blocks = split_every(BLOCK_SIZE, secret)
    blocks.reverse()
    for i in range(len(blocks)-1):
        aes = AES.new(key, AES.MODE_ECB)
        dec = aes.decrypt(blocks[i])
        xor = XOR(dec.encode('hex'), blocks[i+1].encode('hex')).decode('hex') #encode as hex to calculate XOR, the decode back
        plain = xor + plain

    last = blocks[-1]
    aes = AES.new(key, AES.MODE_ECB)
    dec = aes.decrypt(last)
    xor = XOR(dec.encode('hex'), IV.encode('hex')).decode('hex') #encode as hex to calculate XOR, the decode back
    plain = xor + plain
    return plain

def MyCBCencrypt(plaintext, key):
    '''Local CBC encryption procedure implementation'''
    IV = Random.new().read(BLOCK_SIZE) #generate a random Initialization Vector
    ciphertext = IV.encode('hex')
    blocks = split_every(BLOCK_SIZE, plaintext)
    for i in range(len(blocks)):
        xor = XOR(IV.encode('hex'), blocks[i].encode('hex')).decode('hex') # encode to hex to do xor, then decode back
        aes = AES.new(key, AES.MODE_ECB)
        enc = aes.encrypt(xor)
        ciphertext = ciphertext + enc.encode('hex')
        IV = enc
    return ciphertext

def MyCTRdecrypt(ciphertext, key):
    plain = ""
    blocks = split_every(BLOCK_SIZE, ciphertext)
    counter = blocks[0]
    blocks.remove(counter) # first block is the counter

    for b in blocks:
        aes = AES.new(key, AES.MODE_ECB)
        dec = aes.encrypt(counter)

        blockLen = len(b)
        if blockLen < BLOCK_SIZE:
            padded = pad(b.encode('hex'))
            xor = XOR(dec.encode('hex'), padded).decode('hex') # encode to hex to do xor, then decode back. padded is already encoded
            xor = xor[:blockLen] # remove the padding added to compute xor 
        else:
            xor = XOR(dec.encode('hex'), b.encode('hex')).decode('hex') # encode to hex to do xor, then decode back

        plain = plain + xor
        cc = long(counter.encode('hex'), 16) + 1
        counter = hex(cc)[2:-1].decode('hex')
    return plain

def MyCTRencrypt(plaintext, key):
    IV = Random.new().read(BLOCK_SIZE)
    ciphertext = IV.encode('hex') # IV goes at the beggining of ciphertext
    counter = IV.encode('hex')
    blocks = split_every(BLOCK_SIZE, plaintext)
    for block in blocks:
        aes = AES.new(key, AES.MODE_ECB)
        enc = aes.encrypt(counter.decode('hex'))
        blockLen = len(block)
        if blockLen < BLOCK_SIZE:
            padded = pad(block.encode('hex'))
            xor = XOR(enc.encode('hex'), padded).decode('hex') # encode to hex to do xor, then decode back
            xor = xor[:blockLen] # remove the padding added to compute xor
        else:
            xor = XOR(enc.encode('hex'), block.encode('hex')).decode('hex') # encode to hex to do xor, then decode back
        ciphertext = ciphertext + xor.encode('hex')

        #increment counter
        cc = long(counter, 16) + 1
        counter = str(hex(cc))[2:-1]
    return ciphertext




print "\n * CBC encryption... \n"
#inputs is a list with [plaintext, key, ciphertext]
CBCinputs= [
["", "140b41b22a29beb4061bda66b6747e14", "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"],
["", "140b41b22a29beb4061bda66b6747e14", "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"],
["4e657874205468757273646179206f6e65206f66207468652062657374207465616d7320696e2074686520776f726c642077696c6c2066616365206120626967206368616c6c656e676520696e20746865204c696265727461646f72657320646120416d6572696361204368616d70696f6e736869702e", "140b41b22a29beb4061bda66b6747e14", ""],
]
for i in CBCinputs:
    #if lenght is not 3, the input is invalid
    if len(i) != 3:
        print "skipping invalid input..."
        continue

    #the input is hex encoded
    plaintext =  pad(i[0])
    key =        pad(i[1])
    ciphertext = pad(i[2])

    print "key.....:", key
    # if has no plaintext, decode
    if plaintext == "":
        print "ciphered:", ciphertext
        print "==lib===>", CBCdecrypt(ciphertext.decode('hex'), key.decode('hex'))
        print "==mine==>", MyCBCdecrypt(ciphertext.decode('hex'), key.decode('hex')) #decrypt using local method
    else:
        print "plain...:", plaintext.decode('hex')
        print "==lib===>", CBCencrypt(plaintext.decode('hex'), key.decode('hex'))
        mine = MyCBCencrypt(plaintext.decode('hex'), key.decode('hex'))      # encrypt using local method
        print "==mine==>", mine
        print "lib decr>", CBCdecrypt(mine.decode('hex'), key.decode('hex')) # decrypt the result using lib method, to check if encryption is ok.
    print ""





print "\n * CTR encryption...\n"
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

    #the input is hex encoded
    plaintext =  i[0]
    key =        i[1]
    ciphertext = i[2]

    print "key.....:", key
    # if has no plaintext, decode
    if plaintext == "":
        print "ciphered:", ciphertext
        print "==lib===>", CTRdecrypt(ciphertext.decode('hex'), key.decode('hex'))
        mine = MyCTRdecrypt(ciphertext.decode('hex'), key.decode('hex')) #decrypt using local method
        print "==mine==>", mine

    else:
        print "plain...:", plaintext.decode('hex')
        print "==lib===>", CTRencrypt(plaintext.decode('hex'), key.decode('hex'))
        mine = MyCTRencrypt(plaintext.decode('hex'), key.decode('hex'))      # encrypt using local method
        print "==mine==>", mine
        print "lib decr>", CTRdecrypt(mine.decode('hex'), key.decode('hex')) # decrypt the result using lib method, to check if encryption is ok.
    print ""





#!/usr/bin/python

import sys
import re

# constants
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET_LEN = len(ALPHABET)
USAGE = "Usage: {} plaintext.txt somekey\nThe encryption uses this alphabet: {}".format(sys.argv[0], ALPHABET)

# check inputs
if len(sys.argv) < 3:
	print USAGE
	exit(1)

# load plaintext and clean it
filename = sys.argv[1]
plaintext = open(filename, "rt").read().lower()
# remove all non alphabet
regex = re.compile('[^a-zA-Z]', re.MULTILINE)
plaintext = regex.sub("", plaintext)

# pick the key
key = sys.argv[2]

# print result
count = 0
while count < len(plaintext):
	pchar = plaintext[count]
	kchar = key[count%len(key)]
	
	pchar_int = ALPHABET.index(pchar)
	kchar_int = ALPHABET.index(kchar)
	plain_int = (pchar_int + kchar_int)%ALPHABET_LEN

	sys.stdout.write(ALPHABET[plain_int]) 
	count+=1

print ""
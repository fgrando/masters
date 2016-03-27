#!/usr/bin/python

import sets
from fractions import gcd

cyphertext = open("cyphertext.txt", "rt").read()
cyphertext = "ANYVGYSTYNRPLWHRDTKXRNYPVQTGHPHZKFEYUMUSAYWVKZYEZMEZUDLJKTULJLKQBJUQVUECKBNRCTHPKESXMAZOENSXGOLPGNLEEBMMTGCSSVMRSEZMXHLPKJEJHTUPZUEDWKNNNRWAGEEXSLKZUDLJKFIXHTKPIAZMXFACWCTQIDUWBRRLTTKVNAJWVBREAWTNSEZMOECSSVMRSLJMLEEBMMTGAYVIYGHPEMYFARWAOAELUPIUAYYMGEEMJQKSFCGUGYBPJBPZYPJASNNFSTUSSTYVGYS"

cypherlen = len(cyphertext)
print cypherlen

datatable = []

MAX_LENGHT = 20
MIN_LENGHT = 3

for k in range(3, 10):
	print "testing keys with len", k
	datatable.append([k])

	#all possible keys (without repetitions):
	keys = []
	for i in range(0, cypherlen - k):
		key = cyphertext[i:i+k]
		keys.append(key)
	keyset = set(keys)

	for key in list(keyset):
		datatable[-1].append(key) #last element of list

		findings = []
		find = cyphertext.find(key, 0)
		while find > 0:
			findings.append(find)
			find = cyphertext.find(key, find + 1)

		if (findings > k): # filter some trash
			datatable[-1].append(findings)

	#for i in range(0, cypherlen - k):
	#for i in range(0, 5):
	#	key = cyphertext[i:i+k]
	#	datatable[-1].append(key) #last element of list

	#	findings = []
	#	find = cyphertext.find(key, 0)
	#	while find > 0:
	#		findings.append(find)
	#		find = cyphertext.find(key, find + 1)
#
	#	datatable[-1].append(findings)

for k in datatable:
	#print only keys with findings
	for i in range(2, len(k), 2):
		if len(k[i]) > k[0]: # must not include itself...
			print k[i-1], k[i]
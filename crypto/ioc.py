#!/usr/bin/python

import re

print "index of coincidence"
cyphertext = open("cyphertext.txt", "rt").read()
cypherlen = len(cyphertext)
print cypherlen

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w', 'x','y','z']


#cyphertext = "THEREARETWOWAYSOFCONSTRUCTINGASOFTWAREDESIGNONEWAYISTOMAKEITSOSIMPLETHATTHEREAREOBVIOUSLYNODEFICIENCIESANDTHEOTHERWAYISTOMAKEITSOCOMPLICATEDTHATTHEREARENOOBVIOUSDEFICIENCIESTHEFIRSTMETHODISFARMOREDIFFICULT"
#cyphertext = cyphertext.lower()
#cypherlen = len(cyphertext)

table = []
for letter in alphabet:
	ocurrences = len(re.findall(letter, cyphertext))
	percentage = float(ocurrences)/cypherlen
	table.append([letter, ocurrences, percentage])

n = 26
sigma = 0.0
for i in range(0, n):
	ocurrences = table[i][1]
	print table[i]

	sigma = sigma + (ocurrences * (ocurrences -1))

N = cypherlen
IC = sigma/(N*(N-1))
print "IC",IC
#(1 / (cypherlen*(cypherlen - 1)))
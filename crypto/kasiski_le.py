#!/usr/bin/python

import sets
from fractions import gcd


MIN_LENGTH = 5
MAX_LENGTH = 30
MAX_HIST_COLS = 60
HISTOGRAM_CUT = 30 # filter values to be displayed in histogram. The values displayed must be bigger that MAX(histogram)/HISTOGRAM_CUT

SHOW_KEYS = False # more verbose during the process

def natural_factors(n):
	i = 2
	factors = []
	while i <= n:
		if n%i == 0:
			factors.append(i)
		i += 1
	return factors

def print_histogram(hist, title):
	#get the bigger value of histogram
	bigvalue = 0
	for v in hist:
		if v > bigvalue:
			bigvalue = v

	print "histogram (bigger value is = {})".format(bigvalue)
	print title
	for i in range(len(hist)):
		if hist[i] <= bigvalue/HISTOGRAM_CUT:
			continue

		print i, "\t",
		# print histogram bars 
		for j in range(0, int(MAX_HIST_COLS * (float(hist[i])/bigvalue)) ):
			print "-",
		print hist[i]


cyphertext = open("cyphertext.txt", "rt").read()
#cyphertext = "ANYVGYSTYNRPLWHRDTKXRNYPVQTGHPHZKFEYUMUSAYWVKZYEZMEZUDLJKTULJLKQBJUQVUECKBNRCTHPKESXMAZOENSXGOLPGNLEEBMMTGCSSVMRSEZMXHLPKJEJHTUPZUEDWKNNNRWAGEEXSLKZUDLJKFIXHTKPIAZMXFACWCTQIDUWBRRLTTKVNAJWVBREAWTNSEZMOECSSVMRSLJMLEEBMMTGAYVIYGHPEMYFARWAOAELUPIUAYYMGEEMJQKSFCGUGYBPJBPZYPJASNNFSTUSSTYVGYS"

cypherlen = len(cyphertext)
print "text size in characters: {}".format(cypherlen)


if MAX_LENGTH > cypherlen:
	MAX_LENGTH = cypherlen

datatable = []

#findings by key length
histogram = [0] * (MAX_LENGTH+1)
for k in range(MAX_LENGTH, MIN_LENGTH -1, -1):
	if SHOW_KEYS:
		print "testing keys with len", k
	datatable.append([k])

	#generate all possible keys (without repetitions):
	keys = []
	for i in range(0, cypherlen - k):
		key = cyphertext[i:i+k]
		keys.append(key)
	keyset = set(keys)
	
	if SHOW_KEYS:
		print ("all possible keys of size {}:\n\t{}".format(k, ", ".join(list(keyset))))

	for key in list(keyset):
		#save all the found indexes
		findings = []
		find = cyphertext.find(key, 0)
		while find > 0:
			findings.append(find)
			find = cyphertext.find(key, find + 1)
		if len(findings) > 1: # must have at least one repetition
			datatable[-1].append([key,findings])
			histogram[k] += len(findings)

print "\n\nOccurrences accounted..."
print_histogram(histogram, "this shows the number of possible keys by its length.\nkey len | number of findings")

#biggest possible distance = text length
histogram = [0] * (cypherlen+1)

print "processing intervals..."
# check interval and factors
for k in datatable:

	#biggest possible distance = text length
	hist = [0] * (cypherlen+1)

	if SHOW_KEYS:
		print k[0], "found", len(k)-1
	# if at least one possible key was found:
	if len(k) - 1:
		for kk in k:
			# skip the key length
			if k.index(kk) == 0:
				continue
			
			if SHOW_KEYS:
				print "\t",kk

			occurrences = kk[1]
			
			if SHOW_KEYS:
				print("\t\tdistance: {} factors {}".format(occurrences[1] - occurrences[0], natural_factors(occurrences[1] - occurrences[0])))
			
			for f in natural_factors(occurrences[1] - occurrences[0]):
				histogram[f]+=1
				hist[f]+=1
		print "\n\nkey length: {} ({} keys)".format(k[0], len(k) -1)
		# it the 2 possible keys are distant 5 and 17 (primes ;) the number of keys will not match to the max value.
		print_histogram(hist, "the distance between the findings is decomposed in factors. this shows how many times the factors are repeated between different keys with SAME length.\nfactors | occurrences")


print "\n\nfactors of ALL key lengths together"
print_histogram(histogram, "bigger means that the factor belonged to a lot of differences\nfactors | occurrences")

















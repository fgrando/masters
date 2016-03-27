#!/usr/bin/python

KEY_LEN =5
ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ALPHABET_LEN = len(ALPHABET)



print "Calculating IOC for key of size {}".format(KEY_LEN)

cyphertext = open("cyphertext.txt", "rt").read()
#cyphertext = "ANYVGYSTYNRPLWHRDTKXRNYPVQTGHPHZKFEYUMUSAYWVKZYEZMEZUDLJKTULJLKQBJUQVUECKBNRCTHPKESXMAZOENSXGOLPGNLEEBMMTGCSSVMRSEZMXHLPKJEJHTUPZUEDWKNNNRWAGEEXSLKZUDLJKFIXHTKPIAZMXFACWCTQIDUWBRRLTTKVNAJWVBREAWTNSEZMOECSSVMRSLJMLEEBMMTGAYVIYGHPEMYFARWAOAELUPIUAYYMGEEMJQKSFCGUGYBPJBPZYPJASNNFSTUSSTYVGYS".lower()
#print cyphertext

cypherlen = len(cyphertext)
print "text size in characters: {}".format(cypherlen)

alphabets = []

for key in range(KEY_LEN):
	print "alphabet",key

	# set all counters to zero
	alphabet = [0] * ALPHABET_LEN

	count = 0
	while ( (key + (count * KEY_LEN)) <= (cypherlen - 1) ):
		char = cyphertext[key + (count * KEY_LEN)] # at position x
		
		alphabet[ALPHABET.index(char)] += 1
		count += 1

	alphabet_norm = [float(i)/max(alphabet) for i in alphabet]

	alphabets.append(alphabet_norm)


for i in range(ALPHABET_LEN):
	print ALPHABET[i],"\t",
	for k in alphabets:
		if k[i] != 0:
			print round(k[i], 3),
		print "\t",
	print ""

key = "plato"
count = 0
while count < cypherlen:
	ch = cyphertext[count]
	kch = key[count%len(key)]
	
	ch_int = ALPHABET.index(ch)
	kch_int = ALPHABET.index(kch)
	plain = (ch_int - kch_int)%ALPHABET_LEN

	#print "{} {}\t  - \t{} {}\t = \t{}\t\t{}".format(ch, ch_int, kch, kch_int, plain, ALPHABET[plain])
	print ALPHABET[plain],
	count+=1











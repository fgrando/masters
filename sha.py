#!/usr/bin/python
import sys
from Crypto.Hash import SHA256

BLOCK_SIZE_BYTES = 1024

def split_every(n, s):
    return [ s[i:i+n] for i in xrange(0, len(s), n) ]

# check if the file name was informed
if len(sys.argv) < 2:
	print "Usage: {} file".format(sys.argv[0])
	exit(-1)

# the video file
video = sys.argv[1] #"video05.mp4"

# open and load the file
data = open(video, 'rb').read()

# split in blocks
blocks = split_every(BLOCK_SIZE_BYTES, data)

# reverse the block order
blocks.reverse()

# compute the first 
block_hash = SHA256.new(blocks[0]).hexdigest() 
print 0, '\t', block_hash 

totalBlocks = len(blocks)
for i in range(1, totalBlocks):	# ignore first block

	# concatenate hash with another frame
	block_and_hash = blocks[i] + block_hash.decode('hex')

	# compute the new hash
	block_hash = SHA256.new(block_and_hash).hexdigest()

	if i == totalBlocks-1: # last element, first block
		print "h0->", '\t', block_hash
	
	else: # print the hash every n blocks (to reduce verbosity)
		if i%700 == 0:
			print  i, '\t', block_hash

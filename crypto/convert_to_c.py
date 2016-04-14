#!/usr/bin/python
import re
import sys

if len(sys.argv) < 2:
	print "provide the input file. Each line will be considered an hex string."
	exit(-1)

print "/* generated from '{}' */".format(sys.argv[1])
print "/* loading hex values into 32 bits integers */"
print "/* the new line (0x2a) at the end of each line is ignored */\n\n\n"

buff = ""



line_counter = 0
word_counter = []
lines = open(sys.argv[1], 'rt').readlines()


for l in lines:
	hex_line = l.strip()
	if len(hex_line) < 1:
		continue

	#if it is not empty, print the line 
	buff = buff + "\n\t/* text {}: {} */\n".format(line_counter+1, hex_line)
	buff = buff + "\t{ "
	words = re.findall('........', hex_line) # 32 bits now
	for word in words:
		if words.index(word) != len(words) -1:
			buff = buff + "0x{}, ".format(word) # print this it this is not the last workd
		else:
			if lines.index(l) != len(lines) -1:
				buff = buff + "0x{}".format(word) + "},\n" # print this to close the array and allow another
			else:
				buff = buff + "0x{}".format(word) + "}\n" # this closes the last array
	word_counter.append(len(words))
	line_counter = line_counter + 1
	
buff = buff + "};\n"


print "#define TOTAL_TEXTS {}".format(line_counter)
print "int SIZES[TOTAL_TEXTS] = { ",
for w in word_counter:
	if word_counter.index(w) != len(word_counter) -1:
		print "{},".format(w),
	else:
		print "{}".format(w),"};"

print "\n\n"
print "int TEXTS[{}][{}] = ".format(line_counter, max(word_counter)), "{"
print buff
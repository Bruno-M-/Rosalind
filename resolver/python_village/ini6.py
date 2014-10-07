#!/usr/bin/python

import sys

try:
	file_name = sys.argv[1]
except:
	print "Error "+sys.argv[0]+" no input file"
	exit(1)

try: 
	fd = open(file_name, 'r')
except:
	print "Error ["+sys.argv[0]+"] Input ("+file_name+") must be a valid file"
	exit(1)

word = []
word_count = []

for line in fd:
	for index in range(0, len(line.split())):
			element = line.split()[index]
			if line.split()[index] in word:
				for count in range(0, len(word)):
					if word[count] == element:
						word_count[count] += 1
			else:
				word.append(element)
				word_count.append(1)

for count in range(0, len(word)):
	print word[count], word_count[count]


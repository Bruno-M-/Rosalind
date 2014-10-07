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

sample = []

for line in fd:
	sample.append(line[:-1])

for count in range(1, len(sample)+1):
	if count % 2 == 0:
		print sample[count-1]


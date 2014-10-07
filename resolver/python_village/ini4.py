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

sample = fd.readline()
result = 0

for count in range(int(sample.split()[0]), int(sample.split()[1])+1):
	if count % 2 != 0:
		result += count

print result


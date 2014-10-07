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

result = (int(sample.split()[0])**2) + (int(sample.split()[1])**2)

print result



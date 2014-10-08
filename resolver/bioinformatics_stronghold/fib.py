#!/usr/bin/python

import sys
import rosalind

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
month = int(sample.split()[0])
litter = int(sample.split()[1])

print rosalind.fib(month, litter)


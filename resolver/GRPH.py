#!/usr/bin/python

import rosalind
import fasta
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

result = []

result = rosalind.grph(fasta.parser(file_name))

for count in range(0, len(result)):
	print result[count]


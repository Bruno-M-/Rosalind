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


sample = []
consensus = []
count = 0

for line in fd:
	sample.append(line[:-1])
	count += 1

consensus = rosalind.cons(fasta.parser(file_name))


for count in range(4, len(consensus)):
	print consensus[count]

print "A:",
for count in range(0,len(consensus[0])):
	print consensus[0][count],
print
print "C:",
for count in range(0,len(consensus[1])):
	print consensus[1][count],
print
print "G:",
for count in range(0,len(consensus[2])):
	print consensus[2][count],
print
print "T:",
for count in range(0,len(consensus[3])):
	print consensus[3][count],
print

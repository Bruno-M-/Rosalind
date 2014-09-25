#!/usr/bin/python

import string

def dna(s):

	if isinstance(s,type('')):
		sample=s.upper()
		return str(sample.count('A'))+" "+str(sample.count('C'))+" "+str(sample.count('G'))+" "+str(sample.count('T'))
	else:
		print "Error (DNA) Input must be a string"
		return None

def rna(s):

	if isinstance(s,type('')):
		sample=s.upper()
		return sample.replace('T','U')
	else:
		print "Error (RNA) Input must be a string"
		return None

def revc(s):

	if isinstance(s,type('')):
		sample = s[::-1].upper()
		sample = sample.replace('A','t')
		sample = sample.replace('C','g')
		sample = sample.replace('G','c')
		sample = sample.replace('T','a')
		return sample.swapcase()
	else:
		print "Error (REVC) Input must be a string"
		return None




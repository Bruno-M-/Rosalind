#!/usr/bin/python

import string
import sys
import fasta
import protein

def dna(s):

	if isinstance(s,type('')):
		sample=s.upper()
		return str(sample.count('A'))+" "+str(sample.count('C'))+" "+str(sample.count('G'))+" "+str(sample.count('T'))
	else:
		print "Error ["+sys._getframe().f_code.co_name+"] Input must be a string"
		return None

def rna(s):

	if isinstance(s,type('')):
		sample=s.upper()
		return sample.replace('T','U')
	else:
		print "Error ["+sys._getframe().f_code.co_name+"] Input must be a string"
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
		print "Error ["+sys._getframe().f_code.co_name+"] Input must be a string"
		return None


def gc(file_name):

	fasta_array=fasta.parser(file_name)

	if fasta_array != None:
		for element in fasta_array:
			max_sample=[ '', 0 ]
			title, s=element.split('>')
			if isinstance(s,type('')):
				sample=s.upper()
				A, C, G, T=dna(sample).split()
				gc_total=float(C)+float(G)
				total=float(A)+float(C)+float(G)+float(T)
				gc_percent=round(((gc_total/total)*100), 6)
				if max_sample[1] < gc_percent:
					max_sample[0]=title
					max_sample[1]=gc_percent
			else:
				print "Error ["+sys._getframe().f_code.co_name+"] Input must be a string"
				return None
			
		return max_sample
	else:
		return None

def fib(month, litter):

	if (isinstance(month,type(0)) and isinstance(litter,type(0))):
		fibo=0
		f1 = 1
		f2 = 1
		if month > 2:
			for count in range (0, month-2):
				fibo = (f1 + (f2*litter))
				f2 = f1
				f1 = fibo
		else:
			fibo = 1

		return fibo
	else:
		print "Error ["+sys._getframe().f_code.co_name+"] Inputs must be a string"
		return None

def hamm(s1, s2):

	if (isinstance(s1,type('0')) and isinstance(s2,type('0'))):

		if (len(s1) == len(s2)):
			sample1 = s1.upper()
			sample2 = s2.upper()
			hamming_dist=0
			
			if sample1 != sample2:
				for count in range (0,len(sample1)):
					if sample1[count] != sample2[count]:
						hamming_dist += 1

			return hamming_dist
		else:
			print "Error ["+sys._getframe().f_code.co_name+"] Input strings must be the same lenght"
			return None

	else:
		print "Error ["+sys._getframe().f_code.co_name+"] Inputs must be a string"
		return None

def prot(s):

	if isinstance(s,type('0')):
		sample=s.upper()
		prot=''

		for count in range(0, len(sample)/3):
			count_s=count * 3
			prot += protein.translate(sample[count_s:count_s+3])

		return prot


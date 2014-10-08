#!/usr/bin/python

import string
import sys
import fasta
import protein

def dna(s):

	if isinstance(s,type('')):
		sample = s.upper()
		return str(sample.count('A'))+" "+str(sample.count('C'))+" "+str(sample.count('G'))+" "+str(sample.count('T'))
	else:
		print "Error ["+sys._getframe().f_code.co_name+"] Input must be a string"
		return None

def rna(s):

	if isinstance(s,type('')):
		sample = s.upper()
		sample = sample.rstrip('\r\n')
		return sample.replace('T','U')
	else:
		print "Error ["+sys._getframe().f_code.co_name+"] Input must be a string"
		return None

def revc(s):

	if isinstance(s,type('')):
		s= s.rstrip('\r\n')
		sample = s[::-1].upper()
		sample = sample.replace('A','t')
		sample = sample.replace('C','g')
		sample = sample.replace('G','c')
		sample = sample.replace('T','a')
		return sample.swapcase()
	else:
		print "Error ["+sys._getframe().f_code.co_name+"] Input must be a string"
		return None


def gc(fasta_array):

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
			sample1 = sample1.rstrip('\r\n')
			sample2 = sample2.rstrip('\r\n')
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
		sample = sample.rstrip('\r\n')
		prot=''

		for count in range(0, len(sample)/3):
			count_s=count * 3
			prot += protein.translate(sample[count_s:count_s+3])

		return prot

def subs(s1, s2):

	if (isinstance(s1,type('0')) and isinstance (s2,type('0'))):

		if(len(s1)>=len(s2)):
			
			sample1=s1.upper()
			sample2=s2.upper()
			position = []

			index = sample1.find(sample2)
			while (index != -1):
				position.append(index+1)
				index = sample1.find(sample2, index+1)

			return position
		else:
			print "Error ["+sys._getframe().f_code.co_name+"] first strings must be greater or egual to second string"
			return None

	else:
		print "Error ["+sys._getframe().f_code.co_name+"] Inputs must be a string"
		return None

def iprb(k, m, n):

	if (isinstance(k,type(0.0)) and isinstance(m,type(0.0)) and isinstance(n,type(0.0))):

		dominent_proba = [(4.0/4.0),(4.0/4.0),(4.0/4.0),(4.0/4.0),(3.0/4.0),(2.0/4.0),(4.0/4.0),(2.0/4.0),(0.0/4.0)]
		choice_proba = 0
		index = 0
		first_choice_count  = 0
		for first_choice in k, m, n:
			second_choice_count = 0
			for second_choice in k, m, n:
				if (first_choice_count == second_choice_count):
					second_choice -= 1
				choice_proba += ((first_choice/(k+m+n)) * (second_choice/((k+m+n)-1))) * dominent_proba[index]
				index += 1
				second_choice_count += 1
			first_choice_count += 1

		return round(choice_proba, 5)

	else:
		print "Error ["+sys._getframe().f_code.co_name+"] Inputs must be float"
		return None

def fibd(n, m):

	if (isinstance(n,type(0)) and isinstance(m,type(0))):
		fibo=0
		f1 = 1
		f2 = 1
		if n > 2:
			for count in range (3, n+1):
				if (count - m+1) > 1:  
					dead = fibd(count-m+2, m) - fibd(count-m+1,m)
				else:
					dead = 0
				fibo = (f1 + f2) - dead
				f2 = f1
				f1 = fibo
		elif n > 0:
			fibo = 1
		else:
			fibo = 0

		return fibo
	else:
		print "Error ["+sys._getframe().f_code.co_name+"] Inputs must be integer"
		return None

def cons(fasta_array):

	count = 0

	#Get ride of the index part in fasta_raay we don't nedd them
	for element in fasta_array:
		fasta_array[count] = element.split(">")[1]
		count += 1

	A = [0] * len(fasta_array[0])
	C = [0] * len(fasta_array[0])
	G = [0] * len(fasta_array[0])
	T = [0] * len(fasta_array[0])
	consensus = [""] * len(fasta_array[0])


	for count in range(0,len(fasta_array[0])):
		for element in fasta_array:
			if element[count] == "A":
				A[count] += 1
			elif element[count] == "C":
				C[count] += 1
			elif element[count] == "G":
				G[count] += 1
			elif element[count] == "T":
				T[count] += 1
			else:
				print "Error char not recognized"
				return None

	for count in range(0,len(A)):
		#Find max value
		max_nb = 0
		if A[count] > max_nb:
			max_nb = A[count]
		if C[count] > max_nb:
			max_nb = C[count]
		if G[count] > max_nb:
			max_nb = G[count]
		if T[count] > max_nb:
			max_nb = T[count]

		#Find all maxed nucleobase
		if A[count] == max_nb:
			consensus[count] += "A"
		if C[count] == max_nb:
			consensus[count] += "C"
		if G[count] == max_nb:
			consensus[count] += "G"
		if T[count] == max_nb:
			consensus[count] += "T"
	
	#In fact we don't need to compute all possible consensus strings but 
	# I'll keep thoses lines since it works too :)
	#
	##Find how many string we will have to generate
	#cons_nb = 1
	#for count in range(0,len(consensus)):
	#	cons_nb *= len(consensus[count])
	
	result = [""] * 5 #Pre create array that'll hold the consensus string and the 4 profiles
	#cons_pwr = [0] * 4 #Also create this array needed for consensus strings computation

	result[0] = A	
	result[1] = C	
	result[2] = G	
	result[3] = T	

	for count in range(0, len(consensus)):
		result[4] += consensus[count][0]
#		for index in range(4, cons_nb+4):
#			result[index] += consensus[count][index/(len(consensus[count])**cons_pwr[len(consensus[count])])%(len(consensus[count]))]
#
#		cons_pwr[len(consensus[count])] += 1


	return result

def grph (fasta_array):
	
	result = []
	max_size = len(fasta_array)

	for count in range(0, max_size):
		first_label = fasta_array[count].split(">")[0]
		first_sample = fasta_array[count].split(">")[1]
		for index in range(0, max_size):
			second_label = fasta_array[index].split(">")[0]
			second_sample = fasta_array[index].split(">")[1]

			if first_sample != second_sample and first_sample[-3:] == second_sample[:3]:
				result.append(first_label+" "+second_label)

	return result

def iev(sample):

	result = 0.0
	offspring_nb = 2.0
	dominent_proba = [(4.0/4.0),(4.0/4.0),(4.0/4.0),(3.0/4.0),(2.0/4.0),(0.0/4.0)]
	sample_array = sample.split()

	for count in range(0, len(dominent_proba)):
			result += (float(sample_array[count]) * offspring_nb) * dominent_proba[count]

	return result

def lcsm(fasta_array):

	count = 0
	found = True

	#Get ride of the index part in fasta_raay we don't nedd them
	for element in fasta_array:
		fasta_array[count] = element.split(">")[1]
		count += 1

	count = 0

	#Find shortest string in given array

	shortest = 0
	for count in range(0, len(fasta_array)):
		if len(fasta_array[count]) < len(fasta_array[shortest]):
			shortest = count

	# Parse shortest string and try to find decreasing pattern in other samples
	for lenght in range(len(fasta_array[shortest])+1,1,-1):
		max_count = 0
		for index in range(0,(len(fasta_array[shortest])+1)-lenght):
			sample = fasta_array[shortest][index:index+lenght]
			for count in range(1,len(fasta_array)):
				if fasta_array[count].find(sample) == -1:
					found = False
					break
			if found:
				return sample

			found = True
	return None


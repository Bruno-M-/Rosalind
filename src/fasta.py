#
# Parser de fichiers FASTA
#
# Prend en argument un stream
#

import sys

def parser(file_name):
	try: 
		fd = open(file_name, 'r')
	except:
		print "Error ["+sys._getframe().f_code.co_name+"] Input ("+file_name+") must be a valid file"
		return None

	fasta_array=[]
	element=''

	for line in fd:
		if line[0] == '>' :
			if element != '':
				fasta_array.append(element)
			element = line[1:-1]+">"
		else:
			if line != '':
				element += line[:-1]
	
	if element != '':
		fasta_array.append(element)

	return fasta_array


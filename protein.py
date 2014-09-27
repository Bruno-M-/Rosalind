
import sys

def translate(s):

	if isinstance(s,type('')):
		if len(s) == 3:
			sample=s.upper()

			if ( sample == 'UUU' or \
			     sample == 'UUC' \
			   ):
				return 'F'
			elif ( sample == 'CUU' or \
			       sample == 'CUC' or \
			       sample == 'UUA' or \
			       sample == 'CUA' or \
			       sample == 'UUG' or \
			       sample == 'CUG' \
			     ):
				return 'L'
			elif ( sample == 'AUU' or \
			       sample == 'AUA' or \
			       sample == 'AUC' \
			     ):
				return 'I'
			elif ( sample == 'GUU' or \
			       sample == 'GUC' or \
			       sample == 'GUA' or \
			       sample == 'GUG' \
			     ):
				return 'V'
			elif ( sample == 'AUG' ):
				return 'M'
			elif ( sample == 'UCU' or \
			       sample == 'UCC' or \
			       sample == 'UCA' or \
			       sample == 'UCG' or \
			       sample == 'AGU' or \
			       sample == 'AGC' \
			     ):
				return 'S'
			elif ( sample == 'CCU' or \
			       sample == 'CCC' or \
			       sample == 'CCA' or \
			       sample == 'CCG' \
			     ):
				return 'P'
			elif ( sample == 'ACU' or \
			       sample == 'ACC' or \
			       sample == 'ACA' or \
			       sample == 'ACG'
			     ):
				return 'T'
			elif ( sample == 'GCU' or \
			       sample == 'GCC' or \
			       sample == 'GCA' or \
			       sample == 'GCG' \
			     ):
				return 'A'
			elif ( sample == 'UAU' or \
			       sample == 'UAC' \
			     ):
				return 'Y'
			elif ( sample == 'CAU' or \
			       sample == 'CAC' \
			     ):
				return 'H'
			elif ( sample == 'AAU' or \
			       sample == 'AAC' \
			     ):
				return 'N'
			elif ( sample == 'GAU' or \
			       sample == 'GAC' \
			     ):
				return 'D'
			elif ( sample == 'CAA' or \
			       sample == 'CAG' \
			     ):
				return 'Q'
			elif ( sample == 'AAA' or \
			       sample == 'AAG' \
			     ):
				return 'K'
			elif ( sample == 'UGU' or \
			       sample == 'UGC' \
			     ):
				return 'C'
			elif ( sample == 'CGU' or \
			       sample == 'CGC' or \
			       sample == 'CGA' or \
			       sample == 'CGG' or \
			       sample == 'AGA' or \
			       sample == 'AGG' \
			     ):
				return 'R'
			elif ( sample == 'GGU' or \
			       sample == 'GGC' or \
			       sample == 'GGA' or \
			       sample == 'GGG' \
			     ):
				return 'G'
			elif ( sample == 'GAA' or \
			       sample == 'GAG' \
			     ):
				return 'E'
			elif ( sample == 'UGG' ):
				return 'W'
			elif ( sample == 'UAA' or \
			       sample == 'UAG' or \
			       sample == 'UGA' \
			     ):
				return '\n'
			else:
				return None

		else:
			print "Error ["+sys._getframe().f_code.co_name+"] Input string must be length of 3"
			return None
	else:
		print "Error ["+sys._getframe().f_code.co_name+"] Input must be a string"
		return None
			

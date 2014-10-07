#!/usr/bin/python

import os
import sys
import tempfile
import subprocess
import filecmp

std_out = sys.stdout

def hilite(string, status, bold):
	attr = []
	if status == "OK":
		# green
		attr.append('32')
	elif status == "KO":
		# red
		attr.append('31')
	if bold:
		attr.append('1')
	return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

def campaign(directory):

	for dirname, dirnames, filenames in os.walk(directory):

		# For every porblem found
		for filename in filenames:
			problem_name = filename[:-3]
			print problem_name+"\t",
			input_name = "rosalind_"+problem_name+"_dataset.txt"
			output_name = "rosalind_"+problem_name+"_output.txt"

			# Find path to input and output files
			for dirname_2, dirnames_2, filenames_2 in os.walk('.'):
				for filename_2 in filenames_2:
					if filename_2 == input_name:
						input_file = os.path.join(dirname_2, filename_2)
					if filename_2 == output_name:
						output_file = os.path.join(dirname_2, filename_2)
			
			# Create command line with resolver and input file
			cmd = os.path.join(dirname, filename)
			cmd_line = cmd+" "+input_file

			# Create a temporary file to hold result
			result_file = tempfile.NamedTemporaryFile(delete=False)

			# Run the command and get the result
			result_file.write(subprocess.check_output( cmd_line, shell=True))
			result_file.close()

			# Compare the result with the expected output
			if filecmp.cmp(output_file, result_file.name, shallow=False):
				print hilite("[OK]", "OK", True)
			else:
				print hilite("[KO]", "KO", True)
			
			os.remove(result_file.name)


print hilite("********************************","",True)
print hilite("*                              *","",True)
print hilite("*  Rosalind Python Test Suite  *","",True)
print hilite("*                              *","",True)
print hilite("********************************","",True)
print

print hilite("--------------------","",True)
print hilite("|  Python Village  |","",True)
print hilite("--------------------","",True)
print
campaign('../resolver/python_village')

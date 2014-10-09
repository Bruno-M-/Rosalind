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
			input_file = ""
			output_file = ""
			for dirname_2, dirnames_2, filenames_2 in os.walk('.'):
				for filename_2 in filenames_2:
					if filename_2 == input_name:
						input_file = os.path.join(dirname_2, filename_2)
					if filename_2 == output_name:
						output_file = os.path.join(dirname_2, filename_2)
			
			if not os.path.isfile(input_file):
				print hilite("[Missing input file]", "KO", True),
				continue
			if not os.path.isfile(output_file):
				print hilite("[Missing output file]", "KO", True),
				continue

			# Create command line with resolver and input file
			cmd = os.path.join(dirname, filename)
			cmd_line = "time "+cmd+" "+input_file

			# Create a temporary file to hold result
			result_file = tempfile.NamedTemporaryFile(delete=False)
			time_file = tempfile.NamedTemporaryFile(delete=False)

			# Run the command and get the result
			from subprocess import STDOUT
			result_file.write(subprocess.check_output( cmd_line, stderr=STDOUT, shell=True))
			result_file.close()

			# Extract time informations from result file
			fd = open(result_file.name, 'r+')
			lines = fd.readlines()
			time_lines = lines[-3:]
			lines = lines[:-4]
			fd.seek(0)
			fd.truncate()
			fd.writelines(lines)
			fd.close()

			for line in time_lines:
				line = line.replace('\n',' | ')
				line = line.replace('\t',' ')
				time_file.write(line)
			time_file.close()


			# Compare the result with the expected output
			if filecmp.cmp(output_file, result_file.name, shallow=False):
				print hilite("[OK]", "OK", True),
			else:
				print hilite("[KO]", "KO", True),

			fd = open(time_file.name, 'r')
			print fd.readline()[:-3]
			fd.close()
			
			os.remove(result_file.name)
			os.remove(time_file.name)


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
print

print hilite("-------------------------------","",True)
print hilite("|  Bioinformatics Stronghold  |","",True)
print hilite("-------------------------------","",True)
print
campaign('../resolver/bioinformatics_stronghold')
print


from os import listdir
from os.path import isfile, join
import csv

myPath = "C:/Users/Andrew/Documents/495 Data Science-Data/Data/aslinks"
list_of_contents = listdir(myPath)
print(list_of_contents)

inner_path = "C:/Users/Andrew/Documents/495 Data Science-Data/Data/aslinks/cycle-aslinks.l7.t1.c000027.20070913.txt"
this_AS_file_path = inner_path + "/" + listdir(inner_path)[0]
this_AS_file = open(this_AS_file_path, 'r')
file_reader = csv.reader(this_AS_file, delimiter='\t')

# lines_of_file = this_AS_file.readlines()

# Loop through each line of the file and do something with it
for this_line in file_reader:
	if this_line[0] != '#':
		if this_line[0] == 'T':
			# Grab the timestamp info.  We'll need it to populate the link and monitor tables.
			earliest_timestamp = this_line[1]
			latest_timestamp = this_line[2]
		elif this_line[0] == 'M':
			monitor_ip = this_line[1]
			monitor_AS = this_line[2]
			monitor_key = this_line[3]
		elif this_line[0] == 'D':
			num_monitors = len(this_line) - 3
			from_AS = this_line[1]
			to_AS = this_line[2]
		elif this_line[0] == 'I':
			break
from os import listdir, chdir
from os.path import isfile, join
import csv

# function that removes '_' and ',' from AS_number
# We need this because, for now, we are ignoring multi-origin ASes (underscores) and AS sets (commas)
# @param as_num - the AS number, as a string, which could actually be multi-origin or an AS set
# @return the first AS in the list or set
def clean_as(as_num):
	idx = as_num.find(',')


myPath = "C:/Users/Andrew/Documents/495 Data Science-Data/Data/aslinks"
list_of_contents = listdir(myPath)
print(list_of_contents)

# Create the CSV files and objects to receive the data
chdir(myPath)									# change to the desired directory

time_periods_csv = open("time_periods.csv", 'w')		# create file (overwrite old)
time_periods_csv.close()								# close file
timeperiod_ID = 0										# initialize unique ID

monitors_data = {}								# dictionary of [monitor_ip : (ip_version, monitor_as)]
												# we'll carry this dictionary around the whole time--it shouldn't get too big
monitor_change_count = 0						# keep track of how many monitors change AS

ases_data = {}									# dictionary of [AS_number : 1]
												# just using a dictionary here to avoid duplicates.  The value 1 is meaningless

monitor_tp_jct_csv = open("monitor-tp_jct.csv", 'w')	# create junction object b/t monitors and time periods
monitor_tp_jct_csv.close()								# close file

as_links_direct_csv = open("as_links_direct.csv", 'w')	# Create file for Direct AS links
as_links_direct_csv.close()								# close file
asld_ID = 0												# initialize unique ID

asld_monitor_jct_csv = open("asld-monitor_jct.csv", 'w')	# Create junction object for Direct AS Links and Monitors
asld_monitor_jct_csv.close()								# close file

as_links_indirect_csv = open("as_links_indirect.csv", 'w')	# Create file for Indirect AS links
as_links_indirect_csv.close()								# close file
asli_ID = 0													# initialize unique ID

asli_monitor_jct_csv = open("asli-monitor_jct.csv", 'a')	# Create junction object for Indirect AS Links and Monitors
asli_monitor_jct_csv.close()								# close file


inner_path = "C:/Users/Andrew/Documents/495 Data Science-Data/Data/aslinks/cycle-aslinks.l7.t1.c000027.20070913.txt"
ip_version = "IPv4"
this_AS_file_path = inner_path + "/" + listdir(inner_path)[0]
this_AS_file = open(this_AS_file_path, 'r')
file_reader = csv.reader(this_AS_file, delimiter='\t')

# lines_of_file = this_AS_file.readlines()

# Each file has its own mapping of keys to monitors
key_monitor_map = {}	# empty dictionary of (key : monitor_ip)

chdir(myPath)									# change to the directory containing the csv files

time_periods_csv = open("time_periods.csv", 'a')
monitor_tp_jct_csv = open("monitor-tp_jct.csv", 'a')	# open junction object b/t monitors and time periods
as_links_direct_csv = open('as_links_direct.csv', 'a')
asld_monitor_jct_csv = open("asld-monitor_jct.csv", 'a')	# junction obj b/t direct links and monitors that observed those links
as_links_indirect_csv = open("as_links_indirect.csv", 'a')
asli_monitor_jct_csv = open("asli_monitor_jct.csv", 'a')


# Loop through each line of the file and do something with it
for this_line in file_reader:
	if this_line[0] != '#':
		if this_line[0] == 'T':
			# Grab the timestamp info
			earliest_timestamp = this_line[1]
			latest_timestamp = this_line[2]

			# Place info into csv (unsorted)
			time_periods_csv.write(str(timeperiod_ID) + ',' + earliest_timestamp + ',' + latest_timestamp + '\n')
			timeperiod_ID += 1

		elif this_line[0] == 'M':
			# Grab monitor info
			monitor_ip = this_line[1]
			monitor_AS = this_line[2]
			monitor_key = this_line[3]

			# add to monitor object (checking for AS changes)
			try:
				old_AS = monitors_data[monitor_ip][1]
				if old_AS != monitor_AS:
					monitor_change_count += 1
					monitors_data[monitor_ip] = (ip_version, monitor_AS)
				# else do nothing b/c old_AS hasn't changed
			except Exception:
				# if that ip isn't in our map yet, we put it in
				monitors_data[monitor_ip] = (ip_version, monitor_AS)

			# add monitor to local key:monitor map
			key_monitor_map[monitor_key] = monitor_ip

			# add autonomous system to object
			ases_data[monitor_AS] = 1	# The value 1 is meaningless

			# add records to monitor-TP junction object
			monitor_tp_jct_csv.write(monitor_ip + ',' + str(timeperiod_ID - 1) + ',' + monitor_key + '\n')

		elif this_line[0] == 'D':
			# grab info
			num_monitors = len(this_line) - 3
			from_AS = this_line[1]
			to_AS = this_line[2]

			# add autonomous systems to object
			ases_data[from_AS] = 1		# As above, the value 1 is meaningless
			ases_data[to_AS] = 1

			# add as_link_direct records to CSV
			this_record = str(asld_ID) + ',' + ip_version + ',' + str(timeperiod_ID - 1) + ',' + earliest_timestamp + ',' + latest_timestamp + ','
			this_record += from_AS + ',' + to_AS + '\n'
			as_links_direct_csv.write(this_record)

			# record each monitor that observed that link in junction object
			for i in range(0, num_monitors):
				this_key = this_line[i + 3]
				monitor_ip = key_monitor_map[this_key]
				asld_monitor_jct_csv.write(str(asld_ID) + ',' + monitor_ip + '\n')	# write a record to the csv for each monitor observation
				# note: asld_ID will be lookup to the as_links_direct object, so it stays the same for this entire inner loop

			asld_ID += 1	# now we can increment

		elif this_line[0] == 'I':
			# grab info
			num_monitors = len(this_line) - 4
			from_AS = this_line[1]
			to_AS = this_line[2]
			gap_length = this_line[3]

			# add autonomous systems to object
			ases_data[from_AS] = 1		# As above, the value 1 is meaningless
			ases_data[to_AS] = 1

			# add as_link_indirect records to CSV
			this_record = str(asli_ID) + ',' + ip_version + ',' + str(timeperiod_ID - 1) + ',' + earliest_timestamp + ',' + latest_timestamp + ','
			this_record += from_AS + ',' + to_AS + ',' + gap_length + '\n'
			as_links_indirect_csv.write(this_record)

			# record each monitor that observed that link in junction object
			for i in range(0, num_monitors):
				this_key = this_line[i + 4]
				monitor_ip = key_monitor_map[this_key]
				asli_monitor_jct_csv.write(str(asli_ID) + ',' + monitor_ip + '\n')	# write a record to the csv for each monitor observation
				# note: asli_ID will be lookup to the as_links_indirect object, so it stays the same for this entire inner loop

			asli_ID += 1	# now we can increment



# close file objects
time_periods_csv.close()
monitor_tp_jct_csv.close()
as_links_direct_csv.close()
asld_monitor_jct_csv.close()
as_links_indirect_csv.close()
asli_monitor_jct_csv.close()

# Put monitors_data and ases_data into csv files
monitors_csv = open("monitors.csv", 'w')		# open monitors.csv file
for k in monitors_data.keys():
	monitors_csv.write(k + ',' + monitors_data[k][0] + ',' + monitors_data[k][1] + '\n')
monitors_csv.close()

autonomous_systems_csv = open("autonomous_systems.csv", 'w')
for k in ases_data.keys():
	autonomous_systems_csv.write(k + '\n')
autonomous_systems_csv.close()
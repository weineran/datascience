from os import listdir, chdir
from os.path import isfile, join, getsize
import csv
import datetime
import requests		# for downloading (e.g. GET requests)

class Topology_Data:
	'''
	# This class contains the methods for downloading the CAIDA IPv4 and IPv6 topology data and transforming it into csv files that
	# can be imported into a relational database (e.g. PostgreSQL)
	'''

	# Constructor
	# @param data_path - the local directory containing the raw data files
	# @param csv_path - the local directory where the CSV files will be generated
	def __init__(self, data_path, csv_path):
		self.data_path = data_path
		self.csv_path = csv_path

		self.monitors_data = {}			# dictionary of [monitor_ip : (ip_version, monitor_as)]
										# we'll carry this dictionary around the whole time--it shouldn't get too big
		self.ases_data = {}				# dictionary of [AS_number : 1]
										# just using a dictionary here to avoid duplicates.  The value 1 is meaningless


    # download_data_files
    # @param list_file_path - a file path for a file containing a list of data files available for download
    # @param url_prefix - the URL the files will be downloaded from
    # @param start_date - the earliest data to download
    # @param end_date - the latest data to download
	def download_data_files(self, list_file_path, url_prefix, start_date, end_date):
		list_file = open(list_file_path, 'r')
		file_reader = csv.reader(list_file, delimiter='\t')

		for this_line in file_reader:
			data_file_name = this_line[1]
			file_date = self.get_file_date(data_file_name)

			if file_date >= start_date and file_date <= end_date:
				filename = self.data_path + "/" + data_file_name
				full_url = url_prefix + data_file_name
				r = requests.get(full_url)

				with open(filename, 'wb') as fd:
					for chunk in r.iter_content(chunk_size = 1024*512):
						fd.write(chunk)
		

	# unzip_data_files
	# @param start_date - the earliest data to unzip
    # @param end_date - the latest data to unzip
	def unzip_data_files(self, start_date, end_date):
		x = 1

	# transform_data
	# Transforms the data files to CSV files
	# @param start_date - the earliest data to transform (checks yyyymmdd in filename)
	# @param end_date - the latest data to transform (checks yyyymmdd in filename)
	def transform_data(self, start_date, end_date):
		'''
		# The data comes in multiple text files.  Each file is in this form:
		#
		# 	T	1420200540	1420344760		------------------>	timestamp line:		earliest_timestamp	latest_timestamp
		#	M	193.0.0.168	3333	0	---------------------->	monitor line:		monitor_ip			monitor_as 			monitor_key
		#		more M lines...
		#	D	10012	23720	0	1	2	3	4	5	6	-->	direct link line:	from_AS				to_AS 				monitor_key1	monitor_key2	...
		#	I	10026	10024	1	0	1	2	5	6	------>	indirect link line:	from_AS				to_AS 				gap_length		monitor_key1	monitor_key2	...
		#		more D and I lines intermixed...
		#
		# 	We need to parse these text files, extract the data and place them into CSV files that match our data schema
		'''

		list_of_files = listdir(self.data_path)
		uid_map = {}

		# Create the CSV files and objects to receive the data
		chdir(self.csv_path)									# change to the desired directory

		time_periods_csv = open("time_periods.csv", 'w')		# create file (overwrite old)
		time_periods_csv.close()								# close file
		uid_map['timeperiod_ID'] = 0										# initialize unique ID

		uid_map['monitor_change_count'] = 0				# keep track of how many monitors change AS (slip this into the uid map)

		monitor_tp_jct_csv = open("monitor-tp_jct.csv", 'w')	# create junction object b/t monitors and time periods
		monitor_tp_jct_csv.close()								# close file
		uid_map['mtp_ID'] = 0												# initialize unique ID

		as_links_direct_csv = open("as_links_direct.csv", 'w')	# Create file for Direct AS links
		as_links_direct_csv.close()								# close file
		uid_map['asld_ID'] = 0												# initialize unique ID

		asld_monitor_jct_csv = open("asld-monitor_jct.csv", 'w')	# Create junction object for Direct AS Links and Monitors
		asld_monitor_jct_csv.close()								# close file
		uid_map['asldm_ID'] = 0												# initialize unique ID

		as_links_indirect_csv = open("as_links_indirect.csv", 'w')	# Create file for Indirect AS links
		as_links_indirect_csv.close()								# close file
		uid_map['asli_ID'] = 0													# initialize unique ID

		asli_monitor_jct_csv = open("asli-monitor_jct.csv", 'w')	# Create junction object for Indirect AS Links and Monitors
		asli_monitor_jct_csv.close()								# close file
		uid_map['aslim_ID'] = 0												# initialize unique ID

		for data_file in list_of_files:
			this_AS_file_path = self.data_path + "/" + data_file

			# ipv4 filenames are 43 chars long; ipv6 filenames are 50 chars long
			if len(data_file) < 46:
				ip_version = "IPv4"
			else:
				ip_version = "IPv6"

			file_date = self.get_file_date(data_file)
			print(file_date)
			#inner_path = "C:/Users/Andrew/Documents/495 Data Science-Data/Data/aslinks/cycle-aslinks.l7.t1.c000027.20070913.txt"
			#this_AS_file_path = inner_path + "/" + listdir(inner_path)[0]
			if file_date >= start_date and file_date <= end_date:
				td.transform_file(this_AS_file_path, uid_map, ip_version)
		

		



	# transform_file
	# @param file_path - the path of the data file to transform into CSVs
	# @param uid_map - a map (python passes this by reference) containing the current unique ID values for each table
	# @ip_version - "IPv4" or "IPv6"
	# @side-effects - appends data to CSV files
	def transform_file(self, file_path, uid_map, ip_version):
		print("Transforming " + file_path)
		this_AS_file = open(file_path, 'r')
		file_reader = csv.reader(this_AS_file, delimiter='\t')

		# lines_of_file = this_AS_file.readlines()

		# Each file has its own mapping of keys to monitors
		key_monitor_map = {}	# empty dictionary of (key : monitor_ip)

		chdir(self.csv_path)									# change to the directory containing the csv files

		time_periods_csv = open("time_periods.csv", 'a')
		monitor_tp_jct_csv = open("monitor-tp_jct.csv", 'a')	# open junction object b/t monitors and time periods
		as_links_direct_csv = open('as_links_direct.csv', 'a')
		asld_monitor_jct_csv = open("asld-monitor_jct.csv", 'a')	# junction obj b/t direct links and monitors that observed those links
		as_links_indirect_csv = open("as_links_indirect.csv", 'a')
		asli_monitor_jct_csv = open("asli-monitor_jct.csv", 'a')


		# Loop through each line of the file and do something with it
		for this_line in file_reader:
			if len(this_line) > 0 and this_line[0] != '#':

				# get rid of all commas b/c we just can't handle that right now
				#this_line.replace(',','-')	# replace commas with dashes

				if this_line[0] == 'T':
					# Grab the timestamp info
					earliest_timestamp = this_line[1]
					latest_timestamp = this_line[2]

					# Place info into csv (unsorted)
					time_periods_csv.write(str(uid_map['timeperiod_ID']) + ',' + earliest_timestamp + ',' + latest_timestamp + '\n')
					uid_map['timeperiod_ID'] += 1

				elif this_line[0] == 'M':
					# Grab monitor info
					monitor_ip = this_line[1]
					monitor_AS = clean_AS(this_line[2])
					monitor_key = this_line[3]

					# add to monitor object (checking for AS changes)
					try:
						old_AS = self.monitors_data[monitor_ip][1]
						if old_AS != monitor_AS:
							uid_map['monitor_change_count'] += 1
							self.monitors_data[monitor_ip] = (ip_version, monitor_AS)
						# else do nothing b/c old_AS hasn't changed
					except Exception:
						# if that ip isn't in our map yet, we put it in
						self.monitors_data[monitor_ip] = (ip_version, monitor_AS)

					# add monitor to local key:monitor map
					key_monitor_map[monitor_key] = monitor_ip

					# add autonomous system to object
					self.ases_data[monitor_AS] = 1	# The value 1 is meaningless

					# add records to monitor-TP junction object
					monitor_tp_jct_csv.write(str(uid_map['mtp_ID']) + ',' + monitor_ip + ',' + str(uid_map['timeperiod_ID'] - 1) + ',' + monitor_key + '\n')
					uid_map['mtp_ID'] += 1

				elif this_line[0] == 'D':
					# grab info
					num_monitors = len(this_line) - 3
					from_AS = clean_AS(this_line[1])
					#	print(this_line[1] + '  ---  ' + from_AS)

					to_AS = clean_AS(this_line[2])

					# add autonomous systems to object
					self.ases_data[from_AS] = 1		# As above, the value 1 is meaningless
					self.ases_data[to_AS] = 1

					# add as_link_direct records to CSV
					this_record = str(uid_map['asld_ID']) + ',' + ip_version + ',' + str(uid_map['timeperiod_ID'] - 1) + ',' + earliest_timestamp + ',' + latest_timestamp + ','
					this_record += from_AS + ',' + to_AS + '\n'
					as_links_direct_csv.write(this_record)

					# record each monitor that observed that link in junction object
					for i in range(0, num_monitors):
						this_key = this_line[i + 3]
						monitor_ip = key_monitor_map[this_key]
						asld_monitor_jct_csv.write(str(uid_map['asldm_ID']) + ',' + str(uid_map['asld_ID']) + ',' + monitor_ip + '\n')	# write a record to the csv for each monitor observation
						# note: asld_ID will be lookup to the as_links_direct object, so it stays the same for this entire inner loop
						uid_map['asldm_ID'] += 1	# but we do increment this table's unique ID for each record

					uid_map['asld_ID'] += 1	# now we can increment asld_ID

				elif this_line[0] == 'I':
					# grab info
					num_monitors = len(this_line) - 4
					from_AS = clean_AS(this_line[1])
					to_AS = clean_AS(this_line[2])
					gap_length = this_line[3]

					# add autonomous systems to object
					self.ases_data[from_AS] = 1		# As above, the value 1 is meaningless
					self.ases_data[to_AS] = 1

					# add as_link_indirect records to CSV
					this_record = str(uid_map['asli_ID']) + ',' + ip_version + ',' + str(uid_map['timeperiod_ID'] - 1) + ',' + earliest_timestamp + ',' + latest_timestamp + ','
					this_record += from_AS + ',' + to_AS + ',' + gap_length + '\n'
					as_links_indirect_csv.write(this_record)

					# record each monitor that observed that link in junction object
					for i in range(0, num_monitors):
						this_key = this_line[i + 4]
						monitor_ip = key_monitor_map[this_key]
						asli_monitor_jct_csv.write(str(uid_map['aslim_ID']) + ',' + str(uid_map['asli_ID']) + ',' + monitor_ip + '\n')	# write a record to the csv for each monitor observation
						# note: asli_ID will be lookup to the as_links_indirect object, so it stays the same for this entire inner loop
						uid_map['aslim_ID'] += 1	# but we do increment this table's unique ID for each record

					uid_map['asli_ID'] += 1	# now we can increment



		# close file objects
		time_periods_csv.close()
		monitor_tp_jct_csv.close()
		as_links_direct_csv.close()
		asld_monitor_jct_csv.close()
		as_links_indirect_csv.close()
		asli_monitor_jct_csv.close()

		# Put monitors_data and ases_data into csv files
		monitors_csv = open("monitors.csv", 'w')		# open monitors.csv file
		for k in self.monitors_data.keys():
			monitors_csv.write(k + ',' + self.monitors_data[k][0] + ',' + self.monitors_data[k][1] + '\n')
		monitors_csv.close()

		autonomous_systems_csv = open("autonomous_systems.csv", 'w')
		for k in self.ases_data.keys():
			autonomous_systems_csv.write(k + '\n')
		autonomous_systems_csv.close()

	# get_file_date
	# @param data_file - the filename of a topology data file
	# Parses the filename to extract the date
	def get_file_date(self, data_file):
		# ipv4 filenames are 43 chars long; ipv6 filenames are 50 chars long
		if len(data_file) < 46:
			# ip_version = "IPv4"
			file_year = int(data_file[28:32])
			file_month = int(data_file[32:34])
			file_day = int(data_file[34:36])
		else:
			# ip_version = "IPv6"
			file_year = int(data_file[17:21])
			file_month = int(data_file[21:23])
			file_day = int(data_file[23:25])
		file_date = datetime.date(file_year, file_month, file_day)
		return file_date

######## End of Topology_Data class #####################


# clean_AS
# This is a function that removes '_' and ',' from AS_number
# We need this because, for now, we are ignoring multi-origin ASes (underscores) and AS sets (commas)
# Instead we just use the first AS number in the list
# @param as_num - the AS number, as a string, which could actually be multi-origin or an AS set
# @return the first AS in the list or set
def clean_AS(as_num):
	idx_comma = as_num.find(',')
	idx_underscore = as_num.find('_')
	if idx_comma == -1 and idx_underscore == -1:
		return as_num 		# no changes needed
	elif idx_comma != -1 and idx_underscore != -1:
		if idx_comma < idx_underscore:
			return as_num[:idx_comma]
		else:
			return as_num[:idx_underscore]
	elif idx_comma == -1:
		return as_num[:idx_underscore]
	else:
		return as_num[:idx_comma]




####################
### Begin Script ###
####################
data_path = "C:/Users/Andrew/Documents/495 Data Science-Data/Data/aslinks_gz_files/extracted_files"
csv_path = "C:/Users/Andrew/Documents/495 Data Science-Data/Data/aslinks_CSVs"
list_file_path_ipv4 = "C:/Users/Andrew/OneDrive/Documents/Northwestern/Courses/495-Data-Science/Final Project/ipv4_file_list.txt"
list_file_path_ipv6 = "C:/Users/Andrew/OneDrive/Documents/Northwestern/Courses/495-Data-Science/Final Project/ipv6_file_list.txt"

# instantiate an object
td = Topology_Data(data_path, csv_path)

# download data
download_start_date = datetime.date(2014, 2, 1)
download_end_date = datetime.date(2014, 2, 5)
url_prefix_ipv6 = "http://data.caida.org/datasets/topology/ark/ipv6/as-links.requests/andrewweiner2020@u.northwestern.edu/"
#td.download_data_files(list_file_path_ipv6, url_prefix_ipv6, download_start_date, download_end_date)

# transform data
trans_start_date = datetime.date(2014, 2, 2)
trans_end_date = datetime.date(2014, 2, 4)
td.transform_data(trans_start_date, trans_end_date)

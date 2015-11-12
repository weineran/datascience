import os,sys
import time, datetime

filename = os.path.join(os.getcwd(), 'as_links_direct.csv')
#dt = datetime.datetime(2014,1,1).total_seconds()
#print dt
#sys.exit(0)

def getdatadict(filename):
	data = open(filename, 'r').read()
	data = data.strip().split('\n')
	asdata = []
	for d in data:
		dd = {}
		d = d.strip().split(',')
		fromas = int(d[5].strip())
		toas = int(d[6].strip())
		earlytime = float(d[3].strip())
		latetime = float(d[4].strip())
		ipversion = d[1].strip()
		dseconds = (datetime.datetime.fromtimestamp(earlytime) - datetime.datetime(2014,1,1)).total_seconds()
		week = int(dseconds/(7*24*3600)) +1;
		print week
		dd['fromas'] = fromas
		dd['toas'] = toas
		dd['earlytime'] = earlytime
		dd['latetime'] = latetime
		dd['ipversion'] = ipversion
		dd['week'] = week
		asdata.append(dd)

	print asdata[0]
	print asdata[1]

asdata = getdatadict(filename)
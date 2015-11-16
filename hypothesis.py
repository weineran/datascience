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
		#print week
		dd['fromas'] = fromas
		dd['toas'] = toas
		dd['earlytime'] = earlytime
		dd['latetime'] = latetime
		dd['ipversion'] = ipversion
		dd['week'] = week
		asdata.append(dd)
		#print dd
	print len(asdata)

	return asdata

def getASdegree(asdata):
	datav4 = {}
	datav6 = {}
	for d in asdata:
		fromas = d['fromas']
		toas = d['toas']
		if fromas == toas: continue
		as1 = fromas if fromas < toas else toas
		as2 = toas if fromas < toas else fromas
		ipversion = d['ipversion']
		if ipversion == 'IPv4':
			if not datav4.has_key(as1):
				datav4[as1] = set()
			datav4[as1].add(as2)
			if not datav4.has_key(as2):
				datav4[as2] = set()
			datav4[as2].add(as1)
		else:
			if not datav6.has_key(as1):
				datav6[as1] = set()
			datav6[as1].add(as2)
			if not datav6.has_key(as2):
				datav6[as2] = set()
			datav6[as2].add(as1)
	dataIPv4only = []
	dataIPv4v6 = []
	#print set(datav4.keys())
	#print set(datav6.keys())
	for (k,v) in datav4.iteritems():
		#print '\nAS:', k, 'Links:',v
		links = list(v)
		if k in datav6.keys():
			#links.extend(list(datav6[k]))
			dataIPv4v6.append(len(set(links)))
			#print 'v6:', len(set(datav6[k])),set(datav6[k])
			#print 'IPV4V6','AS:', k,'Degree:',len(set(links))
		else:
			#print 'IPV4', 'AS:' ,k,'Degree:',len(set(links))
			dataIPv4only.append(len(set(links)))
	return dataIPv4only, dataIPv4v6



def getweeklynewASlinks(asdata):
	datav4 = {}
	datav6 = {}
	weeks =set()
	for d in asdata:
		fromas = d['fromas']
		toas = d['toas']
		if fromas == toas: continue
		as1 = fromas if fromas < toas else toas
		as2 = toas if fromas < toas else fromas
		ipversion = d['ipversion']
		week = d['week']
		weeks.add(week)
		if ipversion == 'IPv4':
			if not datav4.has_key(week):
				datav4[week] = set()
			datav4[week].add(str((as1,as2)))
		else:
			if not datav6.has_key(week):
				datav6[week] = set()
			datav6[week].add(str((as1,as2)))
	newIPv4 = []
	newIPv6 = []
	newIPv4perc = []
	newIPv6perc = []
	for w in weeks:
		if w == 1:
			continue
		try:
			if not datav4.has_key(w):
				datav4[w] = []
			newv4 = [x for x in datav4[w] if x not in datav4[w-1]]
			newIPv4.append(len(newv4))
			if len(datav4[w-1]) != 0:
				newIPv4perc.append(float(len(newv4))/len(datav4[w-1])*100.0)
			else:
				newIPv4perc.append(0)
		except:
			pass
		try:
			if not datav6.has_key(w):
				datav6[w] = []
			newv6 = [x for x in datav6[w] if x not in datav6[w-1]]
			newIPv6.append(len(newv6))
			if len(datav6[w-1]) != 0:
				newIPv6perc.append(float(len(newv6))/len(datav6[w-1])*100.0)
			else:
				newIPv6perc.append(0)
		except:
			pass
	return newIPv4, newIPv6, newIPv4perc, newIPv6perc


asdata = getdatadict(filename)
#ASv4degree, ASv4v6degree = getASdegree(asdata)
#print '\nASV4only degree', ASv4degree
#print '\nASv4v6 degree', ASv4v6degree

newv4links, newv6links, newIPv4perc, newIPv6perc = getweeklynewASlinks(asdata)
print '\nweekly newv4links', newv4links
print '\nweekly newv6links', newv6links
print '\nweekly newv4linksperc', newIPv4perc
print '\nweekly newv6linksperc', newIPv6perc



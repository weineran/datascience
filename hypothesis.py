import os


filename = os.path.join(os.getcwd(), 'as_links_direct.csv')

data = open(filename, 'r').read()
data = data.strip().split('\n')
asdata = []
for d in data:
	d = d.strip().split(',')
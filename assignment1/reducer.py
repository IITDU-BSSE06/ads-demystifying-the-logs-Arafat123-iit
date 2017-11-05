#!/usr/bin/python

import sys

Total = 0

for line in sys.stdin:
	#print line
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	ip, rest = data_mapped
	if ip =='10.99.99.186':
		Total=Total+1
print str(Total)

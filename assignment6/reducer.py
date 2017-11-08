#!/usr/bin/python

import sys

count2009 = 0
count2010=0
count2011=0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	year, rest = data_mapped
	if '2009' in year:
		count2009=count2009+1
	if '2010' in year:
		count2010=count2010+1
	if '2011' in year:
		count2011=count2011+1

print '2009'+'\t'+ str(count2009)
print '2010'+'\t'+ str(count2010)
print '2011'+'\t'+ str(count2011)

print 'Year 2011 had the most number of hits'
print count2011

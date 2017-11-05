#!/usr/bin/python


import sys

for line in sys.stdin:
	data = line.strip().split(" - - ")
	if len(data) == 2:
		ip, rest = data
		print "{0}\t{1}".format(ip, rest)

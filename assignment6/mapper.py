#!/usr/bin/python
import urlparse

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		a0, a1 ,a2 ,a3 ,a4 ,a5 ,a6 ,a7 ,a8 ,a9= data
#		path = urlparse.urlparse(a6).path

		print "{0}\t{1}".format(a3,a4)

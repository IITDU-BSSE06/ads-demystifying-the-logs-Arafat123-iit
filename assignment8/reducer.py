#!/usr/bin/python

import sys

maxi=0
salesTotal = 0
oldKey = None
file1=""


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, fullPath = data_mapped

    if oldKey and oldKey != thisKey:
        oldKey = thisKey;
        if salesTotal > maxi:
            maxi=salesTotal
            file1=thisKey
        salesTotal = 0

    oldKey = thisKey
    salesTotal += 1

print file1+'\t'+ str(maxi)

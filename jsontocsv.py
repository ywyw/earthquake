#!/usr/bin/env python

import csv
import json
import re
import sys
import ast
 
headers = ["mag","place","time","updated","tz","url","detail","felt","cdi","mmi","alert","status","tsunami","sig","net","code","ids","sources","types","nst","dmin","rms","gap","magType","type","title","coordinates_lat","coordinates_long","depth","id"]

for line in sys.stdin:
	if "metadata" in line:
		head,line = line.split("\"features\":[")
	if "bbox" in line:
		line,tail = line.split("],\"bbox\"")
	if line.strip() !="]}":
		csvline = []
		for i in range(1,25):
			#print "first item: " , headers[i-1]
			#print "secon item: " , headers[i]
			result = re.search('%s\":(.*),\"%s' % (headers[i-1],headers[i]), line).group(1)
			#print result
			csvline.append(result)
		eqtype = re.search(',\"type\":(.*),\"title',line).group(1)
		#print eqtype
		csvline.append(eqtype)
		title = re.search('title\":(.*)},\"geometry',line).group(1)
		#print title
		csvline.append(title)
		coords = re.search('coordinates\":(.*)},\"id', line).group(1)
		coordslist = ast.literal_eval(coords)
		csvline.extend(coordslist)
		toprint='\t'.join(str(i) for i in csvline)
		print toprint
		#print (["%s\t" % item  for item in csvline])
#print "done"

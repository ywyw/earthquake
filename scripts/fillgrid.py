#!/usr/bin/env python

import math
import datetime
import sys

grids={}
f=open('GSRM_gridded_strain_v2.1.txt','r')
for line in f:
	vals = line.split()
	lat = vals[0]
	lon = vals[1]
	vor = vals[5]
	grids[lat,lon]=vor
f.close()
avggrids={}
f=open('GSRM_average_strain_v2.1.txt','r')
for line in f:
	vals = line.split()
	lat = vals[0]
	lon = vals[1]
	exx = float(vals[2])
	eyy = float(vals[3])
	exy = float(vals[4])
	mag = math.sqrt(2*exx*exx+2*exy*exy+2*eyy*eyy)
	avggrids[lat,lon] = mag
f.close()
for line in sys.stdin:
         line = line.strip()
         vals = line.split('\t')
	 lon = vals[26]
	 lat = vals[27]
	 #lat = vals[0]
	 #lon = vals[1]
	 #print (lat,lon)
	 v1 = str(math.floor(float(lat)*10)/10+0.05)+"0"
	 v2 = str(math.floor(float(lon)*10)/10+0.05)+"0"
	 v3 = str(math.floor(float(lat)*5)/5+0.0)+"00"
	 v4 = str(math.floor(float(lon)*4)/4+0.125)
	 vor = 0
	 mag = 0
	 if (v1, v2) in grids:
	 	#print grids.get((v1,v2))
	 	#print "gridded strain found"
	 	vor = grids.get((v1,v2))
	 if (v3, v4) in avggrids:
	 	#print "avg strain found"
		mag = avggrids.get((v3,v4))
	 #print (v1,v2,v3,v4)
	 print "%s\t%s\t%s" % (line,mag,vor)

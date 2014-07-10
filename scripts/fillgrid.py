#!/usr/bin/env python

import math
import datetime
import sys

grids={}
# extract vorticity from grids on strain
f=open('/home/ec2-user/yuhong/earthquake/GSRM_strain_v2.1.txt','r')
for line in f:
	vals = line.split()
	lat = vals[0]
	lon = vals[1]
	vor = vals[5]
	grids[lat,lon]=vor
f.close()

avggrids={}
# extract strain magnitude from grids on average strain
f=open('/home/ec2-user/yuhong/earthquake/GSRM_average_strain_v2.1.txt','r')
for line in f:
	vals = line.split()
	lat = vals[0]
	lon = vals[1]
	exx = float(vals[2]) # x direction strain
	eyy = float(vals[3]) # y direction strain
	exy = float(vals[4]) # shearing force
    # here we compute mag of strain based on a norm of tensors
	mag = math.sqrt(2*exx*exx+2*exy*exy+2*eyy*eyy)
	avggrids[lat,lon] = mag
f.close()

for line in sys.stdin:
         line = line.strip()
         vals = line.split('\t')
	 lon = vals[30]
	 lat = vals[31]
     # dictionary lookup based on the nearest cell in the world
	 v1 = str(math.floor(float(lat)*10)/10+0.05)+"0"
	 v2 = str(math.floor(float(lon)*10)/10+0.05)+"0"
	 v3 = str(math.floor(float(lat)*5)/5+0.0)+"00"
	 v4 = str(math.floor(float(lon)*4)/4+0.125)
	 vor = 0 # if we don't find the cell, this is an interior point and all values are set to 0
	 mag = 0
	 if (v1, v2) in grids:
	 	vor = grids.get((v1,v2))
	 if (v3, v4) in avggrids:
		mag = avggrids.get((v3,v4))
	 print "%s\t%s\t%s" % (line,mag,vor)

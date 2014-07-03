#!/usr/bin/env python

import math
import datetime
import sys

grids={}
f=open('smallgrid.txt','r')
for line in f:
        vals = line.split()
        lat = vals[0]
        lon = vals[1]
        vor = vals[5]
        grids[lat,lon]=vor
f.close()
for line in sys.stdin:
         line = line.strip()
	 print line


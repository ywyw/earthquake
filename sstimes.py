#!/usr/bin/env python

import ephem
import sys 
for line in sys.stdin:
         line = line.strip()
         words = line.split(',')
	 if (len(words) > 2) :
	         o=ephem.Observer()
		 eqdate = words[0].split('T');
		 o.date=eqdate[0]
        	 o.lat=words[1]
		 o.long=words[2]
        	 s=ephem.Sun()
        	 s.compute()
        	 result=ephem.localtime(o.next_rising(s))
        	 print '%s\t%s' % (result, line)
	 else:
		 print '%s\t%s' % ("",line)
         #print result
#o.lat='38.8348'
#o.long='-122.7442'


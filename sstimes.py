#!/usr/bin/env python

import ephem,datetime
import sys 
for line in sys.stdin:
         line = line.strip()
         vals = line.split('\t')
	 if (len(vals) > 2) :
	         o=ephem.Observer()
		 eqdate = int(vals[2]);
		 o.date=datetime.datetime.fromtimestamp(eqdate/1000)
		 o.lat=vals[27]
		 o.long=vals[26]
        	 #print o.lat
		 #print o.long
		 s=ephem.Sun()
        	 s.compute(o)
		 m=ephem.Moon()
		 m.compute(o.date)
		 try:
			risetime=ephem.date(o.next_rising(s))
                        settime=ephem.date(o.next_setting(s))
                        risediff = risetime-o.date
                        setdiff = settime-o.date 
			#print o.next_rising(s)
		 except (ephem.AlwaysUpError, ephem.NeverUpError):
			risediff=0
			setdiff=0
        		pass
        	 print '%s\t%s\t%s\t%s\t%s' % (o.date, str(m.moon_phase), risediff, setdiff, line)
	 else:
		 print '%s\t%s' % ("",line)
         #print result
#o.lat='38.8348'
#o.long='-122.7442'


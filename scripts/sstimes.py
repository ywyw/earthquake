#!/usr/bin/env python

import ephem,datetime
import sys 
for line in sys.stdin:
         line = line.strip()
         vals = line.split('\t')
	 if (len(vals) > 2) :
	     o=ephem.Observer()
		 eqdate = int(vals[2]) # set the date of observer object
		 o.date=datetime.datetime.fromtimestamp(eqdate/1000)
		 o.lat=vals[27] # set coordinates of observer object
		 o.long=vals[26]
		 s=ephem.Sun()
         s.compute(o) # compute sun rays against observer
		 m=ephem.Moon()
		 m.compute(o.date) # compute moon based on object and date
         # for polar quakes, sunrise/sunset may not happen, catch exception
         try:
			risetime=ephem.date(o.next_rising(s))
            settime=ephem.date(o.next_setting(s))
            risediff = risetime-o.date
            setdiff = settime-o.date 
		 except (ephem.AlwaysUpError, ephem.NeverUpError):
			risediff=0 # if there is no sunrise/sunset, set both to 0 for easy computation
			setdiff=0
        	pass
        	print '%s\t%s\t%s\t%s\t%s' % (o.date, str(m.moon_phase), risediff, setdiff, line)
	 else:
		 print '%s\t%s' % ("",line)


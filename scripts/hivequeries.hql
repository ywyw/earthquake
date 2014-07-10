
-- magnitude, count:
select floor(mag),count(*) from eqsgrid where mag is not null group by floor(mag);

-- year, count, average magnitude:
select year(from_unixtime(bigint(time/1000))),count(*),avg(mag) from eqsgrid group by year(from_unixtime(bigint(time/1000)));

-- vorticity, magnitude:
select floor(mag),avg(abs(vor)) from eqsgrid where mag is not null group by floor(mag);

-- strain magnitude, magnitude:
select floor(mag),avg(strainmag) from eqsgrid where mag is not null group by floor(mag);

-- damage, year:
select year, avg(totdamage) from eqs group by year;

-- deaths, year:
select year, avg(totdeaths) from eqs gropu by year;

-- sunrise diff, count:
select floor(sunrisediff*8)/8,count(*) from eqsgrid group by floor(sunrisediff*8)/8;

-- sunset diff, count:
select floor(sunsetdiff*8)/8,count(*) from eqsgrid group by floor(sunsetdiff*8)/8;

-- moonphase, count:
select floor(moonphase*8)/8,count(*) from eqsgrid group by floor(moonphase*8)/8;

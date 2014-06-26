#!/bin/bash
# since in testing each query is about 2MB and block size is 128MB in cloudera clusters, we can store 64 queries
# or 6/year * 10 years in each HDFS file, conveniently each decade
for i in `seq 1900 2013`
do
    str1="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=$i-01-01T00:00:00&endtime=$i-03-01T00:00:00&format=geojson";
    curl -o eq$i.1.json $str1;
    sleep 5;
    str2="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=$i-03-01T00:00:01&endtime=$i-05-01T00:00:00&format=geojson";
    curl -o eq$i.2.json $str2;
    sleep 5;
    str3="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=$i-05-01T00:00:01&endtime=$i-07-01T00:00:00&format=geojson";
    curl -o eq$i.3.json $str3;
    sleep 5;
    str4="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=$i-07-01T00:00:01&endtime=$i-09-01T00:00:00&format=geojson";
    curl -o eq$i.4.json $str4;
    sleep 5;
    str5="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=$i-09-01T00:00:01&endtime=$i-11-01T00:00:00&format=geojson";
    curl -o eq$i.5.json $str5;
    sleep 5;
    str6="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=$i-11-01T00:00:01&endtime=$i-12-31T23:59:59&format=geojson";
    curl -o eq$i.6.json $str6;
    sleep 5;
done

# We aren't done with this year yet, so we can sneakily do this query to get all the information
str1="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=2014-01-01T00:00:00&endtime=2014-03-01T00:00:00&format=geojson";
curl -o eq2014.1.json $str1;
sleep 5;
str2="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=2014-03-01T00:00:01&endtime=2014-05-01T00:00:00&format=geojson";
curl -o eq2104.2.json $str2;
sleep 5;
str3="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=2014-05-01T00:00:01&endtime=2014-07-01T00:00:00&format=geojson";
curl -o eq2014.3.json $str3;

# Cat decades together to form larger blocks
for i in `seq 190 201`
do
    (cat eq${i}*.*.json; echo) >> usgsjson/${i}0s.json
done


#!/bin/bash

# since block size is 128MB in cloudera clusters, we can store 64 queries,
# or 6/year * 10 years in each HDFS file, conveniently each decade
for i in `seq 1900 2014`
do
    str1="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=$i-01-01T00:00:00&endtime=$i-03-01T00:00:00&format=geojson";
    if [ $(curl --write-out %{http_code} --silent -o eq$i.1.json $str1) -ne 200 ]
        then echo "HTTP [GET] FAILED at $str1";
        exit 1;
    fi
    sleep 5;
    str2="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=$i-03-01T00:00:01&endtime=$i-05-01T00:00:00&format=geojson";
    if [ $(curl --write-out  %{http_code} --silent -o eq$i.2.json $str2) -ne 200 ]
        then echo "HTTP [GET] FAILED at $str2";
        exit 1;
    fi;
    sleep 5;
    str3="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=$i-05-01T00:00:01&endtime=$i-07-01T00:00:00&format=geojson";
    if [ $(curl --write-out %{http_code} --silent -o eq$i.3.json $str3) -ne 200 ]
        then echo "HTTP [GET] FAILED at $str3";
        exit 1;
    fi
    sleep 5;
    str4="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=$i-07-01T00:00:01&endtime=$i-09-01T00:00:00&format=geojson";
    if [ $(curl --write-out %{http_code} --silent -o eq$i.4.json $str4) -ne 200 ]
        then echo "HTTP [GET] FAILED at $str4";
        exit 1;
    fi
    sleep 5;
    str5="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=$i-09-01T00:00:01&endtime=$i-11-01T00:00:00&format=geojson";
    if [ $(curl --write-out %{http_code} --silent -o eq$i.5.json $str5) -ne 200 ]
        then echo "HTTP [GET] FAILED at $str5";
        exit 1;
    fi
    sleep 5;
    str6="http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=$i-11-01T00:00:01&endtime=$i-12-31T23:59:59&format=geojson";
    if [ $(curl  --write-out %{http_code} --silent -o eq$i.6.json $str6) -ne 200 ]
        then echo "HTTP [GET] FAILED at $str6";
        exit 1;
    fi
    sleep 5;
done

# Cat decades together to form larger blocks
for i in `seq 190 201`
do
    (cat eq${i}*.*.json; echo) >> usgsjson/${i}0s.json
done


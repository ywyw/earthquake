GISt - Making sense of earthquake data and models
==========
This project was completed in the span of 3 weeks for the Insight Data Engineering program.

Cluster settings used
==========
Amazon EC2 shared cluster with 7 m1.xlarge machines with cloudera v5, hadoop2.0

Ports
==========
* Cloudera Manager, :7180
* Web API, :5000
* Fluentd webhdfs, :50070

Environment installations used
==========
Python libraries (must be on every machine in cluster for Hadoop Streaming MapReduce jobs):
* sudo easy_install pandas
* sudo yum install python-devel
* sudo yum install gcc
* sudo yum install pyephem
* sudo yum install python-pip

Virtual environment for running the Flask server:
* virtualenv venv
* source venv/bin/activate
* sudo pip install libfreetype6-dev
* sudo pip install matplotlib
* sudo pip install happybase
* nohup hbase thrift start &

Additional configs:
* Set up git repositories
* Set up Fluentd (not used in the final version of this project)

Pipeline Summary
===========

Pipeline Details and Scripts
===========
Batch layer:
* The get*.sh scripts send curl requests to pull in the data to hdfs, providing feedback on success.
Real-time layer:
* Insert cron.txt into crontab for hourly USGS updates and save the data to hdfs, where it can be incrementally added.
JSON to TSV:
* In Hadoop Streaming, jsontotsv.py converts the geojson into a tab delimited file and trims off metadata
TSV calculate astronomical information:
* In Hadoop Streaming, sstimes.py finds sunrise/sunset/moon data for each earthquake.
Add gridded crust deformation data:
* Python library lookup of each earthquake to nearest cell.
Create Hive Tables:
* create_table_eqsgrid.q creates the full fledged tsv table and create_table_damages.q creates a table of the damage data.
Hive queries:
* hivequeries.hql lists a few questions that are relevant to investigate.
HBase Schema design:
*The key is magnitude_timestamp, however since unixtime begins in 1970 and HBase does not elegantly handle negative values, Jan 1 1900 is set to 0 and all values are left zero padded to 13 digits.  If magnitude is null, concatenate the string "null" with the timestamp.
Hive to HBase direct import:
* hivetohbase describes how to accomplish the import
Flask + Happybase REST API:
* realindex.html is the index of the website, each figure is rendered dynamically from tsv, time range and magnitude search gracefully handle null values as well as "null" values

Site
===========
The cluster may go offline after 7/21, but it is hosted here for now:

http://ec2-54-215-207-12.us-west-1.compute.amazonaws.com:5000/earthquake/index.html

Findings
===========
* Earthquake numbers have gone up over the years while average magnitude has decreased
* Damage and deaths spike irregularly but have not increased over time (this is a good thing)
* Small increase in earthquakes before sunrise and after sunset (tidal or temperature influence?)
* No apparent pattern in moon phase
* Strain and vorticity linearly increasing in midrange magnitudes but otherwise uncoupled


create external table eqs (
time STRING,
latitude FLOAT,
longitude FLOAT,
depth FLOAT,
mag FLOAT,
magType STRING,
nst INT,
gap FLOAT,
dmin FLOAT,
rms FLOAT,
net STRING,
id STRING,
updated STRING,
place STRING,
type STRING
)
row format delimited
fields terminated by '\t'
location '/user/ubuntu/csvout';



create external table eqsfromjson2 (
datestr STRING,
sunrisediff FLOAT,
sunsetdiff FLOAT,
moonphase FLOAT,
mag FLOAT,
place STRING,
time BIGINT,
updated BIGINT,
tz INT,
url STRING,
detail STRING,
felt INT,
cdi FLOAT,
mmi FLOAT,
alert STRING,
status STRING,
tsunami INT,
sig INT,
net STRING,
code STRING,
ids STRING,
sources STRING,
types STRING,
nst FLOAT,
dmin FLOAT,
rms FLOAT,
gap FLOAT,
magType STRING,
type STRING,
lat FLOAT,
long FLOAT,
depth FLOAT,
id STRING
)
row format delimited
fields terminated by '\t'
location '/user/ubuntu/ephemcsv';


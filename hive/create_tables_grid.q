
create external table eqsgrid (
datestr STRING,
moonphase FLOAT,
sunrisediff FLOAT,
sunsetdiff FLOAT,
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
id STRING,
long FLOAT,
lat FLOAT,
depth FLOAT,
strainmag FLOAT,
vor FLOAT
)
row format delimited
fields terminated by '\t'
location '/user/ec2-user/yuhong/grids';


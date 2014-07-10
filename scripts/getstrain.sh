#!/bin/bash

# get vectorized grid data
if [ $(curl --write-out %{http_code} --silent -o gridstrain.zip "ftp://ftp.globalquakemodel.org/strain-rate/GSRM_gridded_strain_v2.1.zip") -ne 200 ]
    then echo "Gridded strain failed to download";
    exit 1;
fi
if [ $(curl --write-out %{http_code} --silent -o avgstrain.zip "ftp://ftp.globalquakemodel.org/strain-rate/GSRM_average_strain_v2.1.zip") -ne 200 ]
    then echo "Average strain failed to download";
    exit 1;
fi
unzip gridstrain.zip
unzip avgstrain.zip

#!/bin/bash

# get vectorized grid data
if [ $(curl --write-out %{http_code} --silent -o gridstrain.zip "ftp://ftp.globalquakemodel.org/strain-rate/GSRM_gridded_strain_v2.1.zip") -eq 200 ]
    then echo "Vector strain grid failed to download";
fi
    
if [ $(curl --write-out %{http_code} --silent -o avgstrain.zip ftp://ftp.globalquakemodel.org/strain-rate/GSRM_average_strain_v2.1.zip") -eq 200 ]
    then echo "oh no";
fi
unzip gridstrain.zip
unzip avgstrain.zip

#!/bin/bash

# get all the damage data
curl -o damage "http://www.ngdc.noaa.gov/nndc/struts/results?type_0=Exact&query_0$ID&t=101650&s=13&d=189&dfn=signif.txt"
# get vectorized grid data
curl -o gridstrain.zip ftp://ftp.globalquakemodel.org/strain-rate/GSRM_gridded_strain_v2.1.zip
curl -o avgstrain.zip ftp://ftp.globalquakemodel.org/strain-rate/GSRM_average_strain_v2.1.zip

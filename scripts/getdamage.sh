#!/bin/bash

# get earthquake damage data
if [ $(curl --write-out %{http_code} --silent -o damage.tsv "http://www.ngdc.noaa.gov/nndc/struts/results?type_0=Exact&query_0$ID&t=101650&s=13&d=189&dfn=signif.txt") -ne 200]
    then echo "Damage data failed to download";
    exit 0;
fi


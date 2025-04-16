#! /bin/bash

if [ $# != 2 ]; then
    echo "Error! Expected two arguments: 1) a date (MM-DD-YYYY format) and 2) the replicate ID"
    exit 1
fi

echo "$1" | sed -E "s/([0-9]{2})-([0-9]{2})-([0-9]{4})/\3_\1_\2_$(./step_01_zero_pad.sh $2 4)/"
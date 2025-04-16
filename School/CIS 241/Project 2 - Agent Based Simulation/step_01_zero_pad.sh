#! /bin/bash

if [ $# != 2 ]; then
    echo "Error! Expected two arguments: 1) the number to pad and 2) the length to pad to"
    exit 1
fi

output=""

for ((i = 0; i < $((${2}-${#1})); i++)); do
    output="${output}0"
done

output="${output}${1}"

echo "$output"
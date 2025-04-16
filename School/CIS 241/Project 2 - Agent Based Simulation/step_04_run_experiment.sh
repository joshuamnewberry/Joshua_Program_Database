#! /bin/bash

mkdir data
for ((i = 1; i <= $1; i++)); do
    slug=$(./step_02_create_slug.sh $2 $i)
    seed=$(./step_03_create_seed.sh $slug)
    python3 sim.py $seed > data/$slug.csv
done
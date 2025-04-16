#! /bin/bash

grep -E '^(1[0-5]|[0-9])?[0-9],' all_pokemon.csv | grep -Ev '^15[2-9],' | grep -Ev 'Mega' > pokemon_filtered.csv
## Project 4 - Cellular automata

I have included placeholder files for the code you will need to write. 

Additionally, I have included some example input files. 
Once you've compiled your code, you can run it on an input file via IO redirection: 

```
./a.out < example_inputs/life_small.txt
```

Finally, I also added two python scripts in the `scripts` directory.
You do not need them at all to complete the project, they are just included for fun. 

`gen_random.py` will generate a random grid of alive/dead cells. 

`viz.py` will use pygame to visualize your cellular automata!

If you haven't installed pygame, you'll need to run: 
```
python3 -m pip install pygame
```

Then you can just pipe the output of your program to the python script: 
```
./a.out < example_inputs/life_small.txt | python3 scripts/viz.py
```

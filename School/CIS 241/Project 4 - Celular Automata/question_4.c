// This will contain your main function for question 4
#include "automata.h"
#include <stdio.h>
#include <stdlib.h>

int main() 
{
    Automata automata;
    scanf("%d %d %d", &automata.width, &automata.height, &automata.max_timestep);
    int ch; while ((ch = getchar()) != '\n' && ch != EOF);
    scanf("%d %d %d %d %d %d %d %d %d", &automata.birth_rule[0], &automata.birth_rule[1], &automata.birth_rule[2],
    &automata.birth_rule[3], &automata.birth_rule[4], &automata.birth_rule[5], &automata.birth_rule[6], &automata.birth_rule[7], &automata.birth_rule[8]);
    while ((ch = getchar()) != '\n' && ch != EOF);
    scanf("%d %d %d %d %d %d %d %d %d", &automata.survive_rule[0], &automata.survive_rule[1], &automata.survive_rule[2],
    &automata.survive_rule[3], &automata.survive_rule[4], &automata.survive_rule[5], &automata.survive_rule[6], &automata.survive_rule[7], &automata.survive_rule[8]);
    while ((ch = getchar()) != '\n' && ch != EOF);

    // Printing
    PrintInfo(&automata);
    return 0;
}
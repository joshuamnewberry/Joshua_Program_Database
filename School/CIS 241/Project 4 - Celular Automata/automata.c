// Your automata function definitions will go here
#include "automata.h"
#include <stdio.h>
#include <stdlib.h>

void PrintInfo(Automata* automata)
{
    printf("Dimensions are: %dx%d\n", automata->width, automata->height);
    printf("Will run for %d steps\n", automata->max_timestep);

    int birth_rule_num = 0;
    // Make a list of Birth Rule Numbers (True)
    int birth_lst[8];
    int birth_index = 0;
    for(int i = 0; i < 9; i++)
    {
        if(automata->birth_rule[i])
        {
            birth_lst[birth_index] = i;
            birth_index++;
        }
    }
    // Combine into one number
    if(birth_index > 0)
    {
        for(int i = 0; i < birth_index; i++)
        {
            // Slightly modified copied pow function from math.h (compiler won't link it properly)
            int multiplier = 1;
            for(int j = 0; j < /*exponent*/ birth_index-1-i; j++)
                multiplier *= /*base*/ 10;
            birth_rule_num += multiplier * birth_lst[i];
        }
    }

    int survive_rule_num = 0;
    // Make a list of Birth Rule Numbers (True)
    int survive_lst[8];
    int survive_index = 0;
    for(int i = 0; i < 9; i++)
    {
        if(automata->survive_rule[i])
        {
            survive_lst[survive_index] = i;
            survive_index++;
        }
    }
    // Combine into one number
    if(survive_index > 0)
    {
        for(int i = 0; i < survive_index; i++)
        {
            // Slightly modified copied pow function from math.h (compiler won't link it properly)
            int multiplier = 1;
            for(int j = 0; j < /*exponent*/ survive_index-1-i; j++)
                multiplier *= /*base*/ 10;
            survive_rule_num += multiplier * survive_lst[i];
        }
    }
    
    if(birth_index == 0)
    {
        printf("Rule: B/");
    }
    else
    {
        printf("Rule: B");
        if(automata->birth_rule[0] == 1)
        {
            printf("0");
        }
        printf("%d/", birth_rule_num);
    }
    if(survive_index == 0)
    {
        printf("S\n");
    }
    else
    {
        printf("S");
        if(automata->survive_rule[0] == 1)
        {
            printf("0");
        }
        printf("%d\n", survive_rule_num);
    }
}

void PrintState(Automata* automata)
{
    for(int row = 0; row < automata->height; row++)
    {
        for(int column = 0; column < automata->width; column++)
        {
            printf("%c", automata->data[row*automata->width+column]);
        }
        printf("\n");
    }
}

void UpdateState(Automata* automata)
{
    char* new_data = (char*)malloc(automata->height*automata->width*sizeof(char));
    for(int global_row = 0; global_row < automata->height; global_row++)
    {
        for(int global_column = 0; global_column < automata->width; global_column++)
        {
            int count = 0;
            for(int temp_row = global_row-1; temp_row <= global_row+1; temp_row++)
            {
                int neighbor_row;
                if(temp_row == -1)
                {
                    neighbor_row = automata->height-1;
                }
                else if(temp_row == automata->height)
                {
                    neighbor_row = 0;
                }
                else
                {
                    neighbor_row = temp_row;
                }
                for(int temp_column = global_column-1; temp_column <= global_column+1; temp_column++)
                {
                    int neighbor_column;
                    if(temp_column == -1)
                    {
                        neighbor_column = automata->width-1;
                    }
                    else if(temp_column == automata->width)
                    {
                        neighbor_column = 0;
                    }
                    else
                    {
                        neighbor_column = temp_column;
                    }

                    if((global_row != neighbor_row || global_column != neighbor_column) &&
                    automata->data[neighbor_row*automata->width+neighbor_column] == '#')
                    {
                        count++;
                    }
                }
            }
            if(automata->data[global_row*automata->width+global_column] == '.')
            {
                if(automata->birth_rule[count] == 1)
                {
                    new_data[global_row*automata->width+global_column] = '#';
                }
                else
                {
                    new_data[global_row*automata->width+global_column] = '.';
                }
            }
            else
            {
                if(automata->survive_rule[count] == 1)
                {
                    new_data[global_row*automata->width+global_column] = '#';
                }
                else
                {
                    new_data[global_row*automata->width+global_column] = '.';
                }
            }
        }
    }
    free(automata->data);
    automata->data = new_data;
}
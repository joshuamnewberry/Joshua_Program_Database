#include <stdio.h>
#include <stdlib.h>

int main() 
{   
    char* op_list = (char*)malloc(4*sizeof(char));
    float* val_list = (float*)malloc(4*sizeof(float));
    char op = ' ';
    float val = 0;

    int input = scanf("%c %f", &op, &val);
    int size = 0;

    while(input != EOF)
    {
        if(op == 'g')
        {
            if(val < size)
            {
                printf("%c %f\n", op_list[(int)val], val_list[(int)val]);
            }
        }
        else if(op == 'r')
        {
            float score = 0;
            for(int i = val; i < size; i++)
            {
                if(op_list[i] == 'a')
                {
                    score += val_list[i];
                }
                else if(op_list[i] == 's')
                {
                    score -= val_list[i];
                }
                else if(op_list[i] == 'm')
                {
                    score *= val_list[i];
                }
                else if(op_list[i] == 'd')
                {
                    score /= val_list[i];
                }
            }
            printf("%f\n", score);
        }
        else if(op == 'a' || op == 's' || op == 'm' || op == 'd')
        {
            if(size > 0 && size % 4 == 0)
            {
                op_list = (char*)realloc(op_list, (size+4)*sizeof(char));
                val_list = (float*)realloc(val_list, (size+4)*sizeof(float));
            }
            op_list[size] = op;
            val_list[size] = val;
            size++;
        }
        int ch; while ((ch = getchar()) != '\n' && ch != EOF);
        input = scanf("%c %f", &op, &val);
    }
    free(val_list);
    free(op_list);
    return 0;
}
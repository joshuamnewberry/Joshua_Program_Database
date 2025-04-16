#include <stdio.h>
#include <stdlib.h>

int main() 
{
    float score = 0;
    char op = ' ';
    float val = 0;
    int input = scanf("%c %f", &op, &val);

    while(input != EOF)
    {
        if(op == 'a')
        {
            score += val;
        }
        else if(op == 's')
        {
            score -= val;
        }
        else if(op == 'm')
        {
            score *= val;
        }
        else if(op == 'd')
        {
            score /= val;
        }
        printf("%f\n", score);
        int ch; while ((ch = getchar()) != '\n' && ch != EOF);
        input = scanf("%c %f", &op, &val);
    }
    return 0;
}
// You'll define your Automata struct and function prototypes here
typedef struct Automata 
{
    int width;
    int height;
    int max_timestep;
    int birth_rule[9];
    int survive_rule[9];
    char* data;
} Automata;

void PrintInfo(Automata* automata);

void PrintState(Automata* automata);

void UpdateState(Automata* automata);
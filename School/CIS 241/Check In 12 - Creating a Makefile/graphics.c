#include <stdio.h>

#include "graphics.h"

void DrawBox(char* str, int len){
  int width = len + 10;
  int vertical_padding = 4;
  // Print the top line
  for(int i = 0; i < width; i++){
    printf("-");
  }
  printf("\n");

  // Print first lines of padding
  for(int i = 0; i < vertical_padding; i++){
    printf("|");
    for(int i = 0; i < width - 2; i++){
      printf(" ");
    }
    printf("|\n");
  }
 
  // Print line with string
  printf("|    "); 
  printf("%s", str);
  printf("    |\n"); 

  // Print last lines of padding
  for(int i = 0; i < vertical_padding; i++){
    printf("|");
    for(int i = 0; i < width - 2; i++){
      printf(" ");
    }
    printf("|\n");
  }
  // Print the bottom line
  for(int i = 0; i < width; i++){
    printf("-");
  }
  printf("\n");

}

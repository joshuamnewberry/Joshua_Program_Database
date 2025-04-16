#include <stdio.h>
#include <stdlib.h>

#include "graphics.h"
#include "clown.h"

int main(){
  int length = 0;
  char* laugh_str = MakeLaugh(20, &length);
  DrawBox(laugh_str, length);
  free(laugh_str);
  return 0;
}

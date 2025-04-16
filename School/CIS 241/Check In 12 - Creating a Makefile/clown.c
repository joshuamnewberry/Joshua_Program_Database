#include <stdlib.h>

#include "clown.h"


char* MakeLaugh(int count, int* str_len){
  char* str = (char*)malloc(count * 2 + 1);
  for(int i = 0; i < count; i++){
    str[2 * i] = 'h';
    str[2 * i + 1] = 'a';
  }
  str[0] = 'H';
  str[count * 2] = 0;
  *str_len = count * 2;
  return str;
}

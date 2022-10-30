#include <stdio.h>
#include <string.h>

int main() {
  char cVar1;
  char *str = 0x4c75257240343a4;
  printf("%s", str);
  int strLen;
  long i;
  
  //str = strdup(param_2);
  // 0x4c75257240343a4
  strLen = strlen(str);
  printf("%i", strLen);
  for (i = 0; i < strLen; i = i + 1) {
    if ((' ' < str[i]) && (str[i] != '\x7f')) {
      cVar1 = (char)(str[i] + 0x2f);
      if (str[i] + 0x2f < 0x7f) {
        str[i] = cVar1;
      }
      else {
        str[i] = cVar1 + -0x5e;
      }
    }
  }
  printf("%s", str);
  return 0;
}

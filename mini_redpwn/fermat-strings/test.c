#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
   int val;
   char str[100];
   
   strcpy(str, "4294967295");
   val = atoi(str);
   printf("String value = %s, Int value = %d\n", str, val);

   strcpy(str, "tutorialspoint.com");
   val = atoi(str);
   printf("String value = %s, Int value = %d\n", str, val);

   return(0);
}

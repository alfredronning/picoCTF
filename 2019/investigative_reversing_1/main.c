int main() {
  FILE *flag_file;
  FILE *mystery1_file;
  FILE *mystery2_file;
  FILE *mystery3_file;
  char local_6b;
  int i;
  int i;
  int i;
  char flag_buffer [4];
  char local_34;
  char local_33;
  long local_10;
  
  flag_file = fopen("flag.txt","r");
  mystery1_file = fopen("mystery.png","a");
  mystery2_file = fopen("mystery2.png","a");
  mystery3_file = fopen("mystery3.png","a");
  if (flag_file == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (mystery1_file == (FILE *)0x0) {
    puts("mystery.png is missing, please run this on the server");
  }
  fread(flag_buffer,0x1a,1,flag_file);

  // puts first char of flag plus 0x15 in mystery2 file p
  fputc((int)(char)(flag_buffer[0] + '\x15'),mystery2_file);
  // puts second char of flag in mystery3 file (i)
  fputc((int)flag_buffer[1],mystery3_file);
  // puts third char of flag in mystery3 file (c)
  fputc((int)flag_buffer[2],mystery3_file);
  local_6b = flag_buffer[3]; // o
  // puts 4 and 5 bytes if the flag in myster3 and 1 (C T)
  fputc((int)local_33,mystery3_file);
  fputc((int)local_34,mystery1_file);
  
  for (i = 6; i < 10; i = i + 1) {
    local_6b = local_6b + '\x01';
    fputc((int)flag_buffer[i],mystery1_file);
  }
  fputc((int)local_6b,mystery2_file);
  for (i = 10; i < 0xf; i = i + 1) {
    fputc((int)flag_buffer[i],mystery3_file);
  }
  for (i = 0xf; i < 0x1a; i = i + 1) {
    fputc((int)flag_buffer[i],mystery1_file);
  }
  return;
  // mystery.png CF{An1_9a47141}
  // mystert3.png icT0tha_
  // picoCTF{An0tha_1_9a47141}
}



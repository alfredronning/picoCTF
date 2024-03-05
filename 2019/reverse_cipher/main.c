void main(){
  size_t sVar1;
  char flag_buffer [23];
  char local_41;
  int local_2c;
  FILE *rev_file;
  FILE *flag_file;
  uint j;
  int i;
  char flag_char;
  
  flag_file = fopen("flag.txt","r");
  rev_file = fopen("rev_this","a");
  if (flag_file == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (rev_file == (FILE *)0x0) {
    puts("please run this on the server");
  }
  sVar1 = fread(flag_buffer,0x18,1,flag_file);
  local_2c = (int)sVar1;
  if ((int)sVar1 < 1) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  for (i = 0; i < 8; i = i + 1) {
    flag_char = flag_buffer[i];
    fputc((int)flag_char,rev_file);
  }
  for (j = 8; (int)j < 0x17; j = j + 1) {
      // if j is even add 0x5 to the byte
    if ((j & 1) == 0) {
      flag_char = flag_buffer[(int)j] + '\x05';
    }
     // if j is odd subtract 0x2 to the byte
    else {
      flag_char = flag_buffer[(int)j] + -2;
    }
    fputc((int)flag_char,rev_file);
  }
  flag_char = local_41;
  fputc((int)local_41,rev_file);
  fclose(rev_file);
  fclose(flag_file);
  return;
}

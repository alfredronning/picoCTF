int main() {
  size_t file_status;
  char original_buffer;
  char encoded_char;
  int i;
  int j;
  int flag_position;
  FILE *flag_file;
  FILE *original_file;
  FILE *encoded_file;
  char flag_buffer [56];
  
  flag_file = fopen("flag.txt","r");
  original_file = fopen("original.bmp","r");
  encoded_file = fopen("encoded.bmp","a");
  if (flag_file == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (original_file == (FILE *)0x0) {
    puts("original.bmp is missing, please run this on the server");
  }
  file_status = fread(&original_buffer,1,1,original_file);
  flag_position = 2000;
  // Moves first 2k bytes from original into encoded file buffer
  for (i = 0; i < flag_position; i = i + 1) {
    fputc((int)original_buffer,encoded_file);
    file_status = fread(&original_buffer,1,1,original_file);
  }
  file_status = fread(flag_buffer,0x32,1,flag_file);
  if (file_status < 1) {
    puts("flag is not 50 chars");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  // loops through every 0x32 bytes in the flag
  for (i = 0; i < 0x32; i = i + 1) {
      // loops 8 times and calls the codedChar function to produce 8 encoded chars per flagbyte
    for (j = 0; j < 8; j = j + 1) {
      encoded_char = codedChar(j,(int)(char)(flag_buffer[i]-5),(int)original_buffer);
      // writes 400 bytes onto the 8 per byte in the flag
      fputc((int)encoded_char,encoded_file);
      fread(&original_buffer,1,1,original_file);
    }
  }
  // writes all the remainding bytes to the encoded file
  while (file_status == 1) {
    fputc((int)original_buffer,encoded_file);
    file_status = fread(&original_buffer,1,1,original_file);
    file_status = (int)file_status;
  }
}



byte codedChar(int j, byte flag_char, byte original_char){
  if (j != 0) {
      // thes the j-th bit from the flag byte j=0 will be the first bit, and j=7 the last
    flag_char = flag_char >> ((byte)j & 0x1f);
  }
  // takes first 7 bits from the original byte, and the last one from the encoded flag bit
  return original_char & 0xfe | flag_char & 1;
}

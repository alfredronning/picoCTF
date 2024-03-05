
void FUN_00010078(byte *zero_to_256,long param_2,ulong mod_param)

{
  byte bVar1;
  ulong uVar3;
  ulong uVar5;
  
  zero_to_256 = [i for i in range(256)]
  uVar5 = 0;
  for i in range(256):
    uVar3 = i % mod_param;
    bVar1 = *zero_to_256;
    uVar3 = (ulong)(int)((int)uVar5 + (uint)*(byte *)(uVar3 + param_2) + (uint)bVar1);
    uVar5 = uVar3 & 0xff;
    *zero_to_256 = zero_to_256[uVar3 & 0xff];
    zero_to_256[uVar3 & 0xff] = bVar1;
    zero_to_256 = pbVar6 + 1;
  return;
}

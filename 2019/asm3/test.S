# ebp + 4 = 0xd2c26416
# ebp + 8 = 0xe6cf51f0
# ebp + 12 = 0xe54409d5

asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax
	<+5>:	mov    ah,BYTE PTR [ebp+0x9] # ah = 4409d500 00 00 00 00
	<+8>:	shl    ax,0x10 # nullstille
	<+12>:	sub    al,BYTE PTR [ebp+0xe]
	<+15>:	add    ah,BYTE PTR [ebp+0xf]
	<+18>:	xor    ax,WORD PTR [ebp+0x12]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret    


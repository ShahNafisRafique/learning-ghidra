passwd=[0x95, 0xb3, 0x15, 0x32, 0xe4, 0xe4, 0x43, 0x6b, 0x90, 0xbe, 0x1b, 0x31, 0xa7, 0x8b, 0x2d, 0x05]

i =0

while(i <len(passwd)):
    passwd[i] ^= 0Xa7
    passwd[i+1] ^= 0x8b
    passwd[i+2] ^= 0x2d
    passwd[i+3] ^= 5
    i += 4

for c in passwd:
    print(chr(c),end="")
print("")

for c in passwd:
    print(hex(c)[2:],end="")
print("")
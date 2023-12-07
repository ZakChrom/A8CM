#!/bin/sh
set -xe
~/Software/Yabal/yabal/yabal build ./main.yabal 
~/Programming/Aslion/zig-out/bin/main ~/Programming/YabalTest/main.asm $1

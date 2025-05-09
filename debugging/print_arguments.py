#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("No arguments provided. Usage: ./script.py arg1 arg2 ...")
else:
    for arg in sys.argv[1:]:
        print(arg)


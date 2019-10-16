#!/usr/bin/python3
from sys import argv
from urllib.parse import unquote
import base64

def main():
    try:
        script, mode, cipher = argv
        if mode == "-u":
            res = unquote(cipher)
            print()
            print()
            print("Result")
            print("------")
            print(res)
        elif mode == "-b":
            b64_string = cipher
            b64_string += "=" * ((4 - len(b64_string) % 4) % 4)
            plain = base64.b64decode(b64_string)
            print()
            print()
            print("Result")
            print("------")
            print(plain)
    except:
        print()
        print("Usage: python3 decoding -u | -b xxxxx")
        print()


if __name__ == "__main__":
    main()

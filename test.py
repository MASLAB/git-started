#!/usr/bin/python3

def failure():
    print("Oh no!  There's a bug!")
    print("[ERROR] `test.py` failed")

def success():
    print("Yay!  You fixed the bug!")
    print("`test.py` completed with no errors")

if __name__ == "__main__":
    success()
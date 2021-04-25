#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Sun,Apr25/2020
# This program does basic math


def main():
    # To calculate Area :
    L = int(input("please enter the length:"))
    W = int(input("please enter the width:"))
    calculation =  L * W
    print("Area =", calculation)
    # To calculate perimeter :
    l = int(input("please enter the length:"))
    w = int(input("please enter the width:"))
    calculation =  2 *(l + w)
    print("Perimeter =", calculation)

if __name__ == "__main__":
    main()
    
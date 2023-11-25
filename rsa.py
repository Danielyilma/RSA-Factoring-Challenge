#!/usr/bin/python3
import sys
import math

def prime(num):
    j = math.isqrt(num)
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % j == 0:
            return False
        if num % i == 0:
            return False
        j -= 1
    return True

def divisiblity(num):
    if num % 2 == 0:
        if prime(num // 2):
            return 2
    for i in range(3, num, 2):
        if prime(i) and num % i == 0:
            print(i)
            if prime(num // i):
                return i


if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit()

file = open(sys.argv[1], "r")

for line in file:
    number = int(line)
    if prime(number):
        print("{}={}*{}".format(number, number, 1))
    else:
        i = int(divisiblity(number))
        print("{}={}*{}".format(number, number // i, i))



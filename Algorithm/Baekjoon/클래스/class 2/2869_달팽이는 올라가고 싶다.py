from math import ceil
import sys

A, B, V = map(int, sys.stdin.readline().split())

print(ceil((V-B) / (A-B)))
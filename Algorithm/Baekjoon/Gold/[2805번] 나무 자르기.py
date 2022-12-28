import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split())

trees = Counter(list(map(int, input().split())))

def binary(h, target):
    left, right = 0, h
    while left <= right:
        middle = (left+right)//2
        total = sum((tree-middle)*cnt for tree, cnt in trees.items() if tree > middle)
        left, right = (left, middle-1) if total - target < 0 else (middle+1, right)
    return right

print(binary(max(trees), M))
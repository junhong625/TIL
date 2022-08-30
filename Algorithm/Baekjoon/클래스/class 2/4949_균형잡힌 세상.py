import sys

while True:
    sentence = sys.stdin.readline()
    if sentence[0] == '.':
        break
    stack = []
    for char in sentence:
        if char in '()[]':
            if stack and stack[-1]+char in ['()', '[]']:
                stack.pop()
            else:
                stack.append(char)
    print('no' if stack else 'yes')
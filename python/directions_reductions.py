# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

def dirReduc(arr):
    opposite = { "NORTH": "SOUTH", "SOUTH": "NORTH", "WEST": "EAST", "EAST": "WEST"}
    stack = []

    for i in arr:
        if len(stack) == 0 or stack[-1] != opposite[i]:
            stack.append(i)
            continue
        stack.pop()
    return stack
#! /usr/bin/env python3

import sys

def run(input):
    input_list = list(map(lambda i: int(i), list(input)))
    length = len(input_list)
    sum = 0
    for i in range(0, length):
        j = int((i + length/2) % length)
        if input_list[i] == input_list[j]:
            sum += input_list[i]
    return str(sum)

if __name__ == '__main__':
    print(run(sys.stdin.read().strip()))
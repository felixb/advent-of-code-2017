#! /usr/bin/env python3

import sys
from functools import reduce

def parse_line(line):
    if len(line) == 0:
        return 0
    input = [int(i) for i in filter(lambda i: i != '', line)]
    return max(input) - min(input)

def run(input):
    input_matrix =  list(map(lambda i: i.split(' '), input.split("\n")))
    return str(reduce(lambda x,y: x+y, map(parse_line, input_matrix)))

if __name__ == '__main__':
    print(run(sys.stdin.read().strip()))
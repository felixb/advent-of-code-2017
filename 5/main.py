#! /usr/bin/env python3

import sys


def run_1(input):
    instructions = [int(i) for i in input.split("\n")]
    pos = 0
    i = 0
    while pos >= 0 and pos < len(instructions):
        i += 1
        cmd = instructions[pos]
        instructions[pos] += 1
        pos += cmd
    return i


def run_2(input):
    instructions = [int(i) for i in input.split("\n")]
    pos = 0
    i = 0
    while pos >= 0 and pos < len(instructions):
        i += 1
        cmd = instructions[pos]
        if cmd >= 3:
            instructions[pos] -= 1
        else:
            instructions[pos] += 1
        pos += cmd
    return i


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read().strip()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read().strip()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])

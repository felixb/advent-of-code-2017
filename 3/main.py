#! /usr/bin/env python3

import sys

DIRECTIONS = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
]


def distance_to_zero(pos):
    return abs(pos[0]) + abs(pos[1])


def step(pos, direction, length):
    return [
        pos[0] + direction[0] * length,
        pos[1] + direction[1] * length,
    ]


def run_1(input):
    target = int(input)
    pos = [0, 0]
    step_length = 1
    step_count = 0
    value = 1
    while value < target:
        step_length = min(step_length, target - value)
        pos = step(pos, DIRECTIONS[step_count % 4], step_length)
        value += step_length
        step_length += step_count % 2
        step_count += 1
    return distance_to_zero(pos)


def run_2(input):
    return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read().strip()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read().strip()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])

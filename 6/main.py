#! /usr/bin/env python3

import re
import sys


def run_var(input, variant):
    banks = [int(i) for i in re.compile("\s+").split(input)]
    num_banks = len(banks)
    configurations = []
    while banks not in configurations:
        configurations += [banks[:]]
        # find the bank with the most blocks
        peak_index = 0
        for i in range(0, num_banks):
            if banks[i] > banks[peak_index]:
                peak_index = i
        # distribute the blocks to all the banks
        num_blocks = banks[peak_index]
        banks[peak_index] = 0
        for i in range(0, num_blocks):
            banks[(peak_index + i + 1) % num_banks] += 1
    if variant == 1:
        return len(configurations)
    else:
        num_configurations = len(configurations)
        for i in range(0, num_configurations):
            if configurations[i] == banks:
                return num_configurations - i
        return None


def run_1(input):
    return run_var(input, 1)


def run_2(input):
    return run_var(input, 2)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read().strip()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read().strip()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])

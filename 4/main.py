#! /usr/bin/env python3

import sys


def is_valid_passphrase(p):
    words = p.split(" ")
    return len(words) == len(set(words))


def run_1(input):
    passphrases = input.split("\n")
    valid_passphrases = 0
    for p in passphrases:
        if is_valid_passphrase(p):
            valid_passphrases += 1
    return valid_passphrases


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

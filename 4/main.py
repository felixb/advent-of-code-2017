#! /usr/bin/env python3

import sys


def is_valid_passphrase_1(p):
    words = p.split(" ")
    return len(words) == len(set(words))


def is_valid_passphrase_2(p):
    all_words = p.split(" ")
    sorted_words = ["".join(sorted(list(w))) for w in all_words]
    return len(sorted_words) == len(set(sorted_words))


def is_valid_passphrase(p, variant):
    if variant == 1:
        return is_valid_passphrase_1(p)
    else:
        return is_valid_passphrase_2(p)


def validate_passpfharses(input, variant):
    passphrases = input.split("\n")
    valid_passphrases = 0
    for p in passphrases:
        if is_valid_passphrase(p, variant):
            valid_passphrases += 1
    return valid_passphrases


def run_1(input):
    return validate_passpfharses(input, 1)


def run_2(input):
    return validate_passpfharses(input, 2)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s (1|2)' % sys.argv[0])
    if sys.argv[1] == '1':
        print(run_1(sys.stdin.read().strip()))
    elif sys.argv[1] == '2':
        print(run_2(sys.stdin.read().strip()))
    else:
        sys.exit('Unknown action: %s' % sys.argv[1])

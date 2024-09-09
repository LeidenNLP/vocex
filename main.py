#!/usr/bin/env python3

import sys

"""
Read a text.
Tokenize it.
Extract its vocabulary.
Output the vocabulary.
"""

def main():
    text = sys.stdin.read()
    tokens = text.lower().split()
    vocab = set(tokens)
    sys.stdout.write('\n'.join(sorted(vocab)))



if __name__ == '__main__':
    main()


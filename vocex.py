import sys
import wordcloud    # not actually used; only meant to illustrate how dependencies work

"""
Read a text.
Tokenize it.
Extract its vocabulary.
Output the vocabulary.
"""

def cli():
    text = sys.stdin.read()
    tokens = text.lower().split()
    vocab = set(tokens)
    sys.stdout.write('\n'.join(sorted(vocab)))



if __name__ == '__main__':
    cli()


import sys
import wordcloud    # not actually used; only meant to illustrate how dependencies work (see it in the pyproject.toml file?)

"""
A very simplistic, minimalist vocabulary extractor, to illustrate the basics of command-line tools and packaging.
"""


def cli():
    """
    Command-line interface, just an input-output wrapper around the function extract_vocabulary.
    """
    text = sys.stdin.read()
    vocab = extract_vocabulary(text)
    sys.stdout.write('\n'.join(vocab))


def extract_vocabulary(text):
    """
    Function doing the heavy-lifting.
    """
    tokens = text.lower().split()
    vocab = set(tokens)
    vocab_sorted = sorted(vocab)
    return vocab_sorted


if __name__ == '__main__':
    cli()


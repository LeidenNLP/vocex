# Vocex: Vocabulary extractor

This is a minimal example project for the course Python for Linguists 2, to illustrate creating pip-installable tools.

## Installation

You can just do:

```bash
pip install git+https://github.com/leidennlp/vocex
```

`pip` will install this program in the currently active Python environment, which can sometimes be what you want; the `vocex` command will be available whenever that environment is activated.

However, for tools that you intend to use regardless of virtual environment, it is advisable to use `pipx`. First install `pipx` itself, see [these instructions](https://github.com/pypa/pipx). Then you can do:

```bash
pipx install git+https://github.com/leidennlp/vocex
```

This creates a virtual environment specifically for this program, but makes the `vocex` command available globally. 

## Usage

Here is a basic usage, piping text into it using the bash pipe `|`, and redirecting its output to a file (`>`):

```bash
$ cat some_text.txt | vocex > vocab.txt
```

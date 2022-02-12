import importlib.util
import pycli
import sys

# expose example command line interface package 'example/cli'
if not importlib.util.find_spec("cli"):
    sys.path.append("example")

# set sys.argv and run pycli
def run (argv: list[str] = []):
    sys.argv = ["main"] + argv
    return pycli.run("cli")

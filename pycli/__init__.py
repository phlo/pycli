"""Modularized command line tools made easy."""

__version__ = "0.1"
__license__ = "MIT"
__author__  = "Florian Schrögendorfer"
__email__   = "florian.schroegendorfer@jku.at"
__url__     = "https://gitlab.sai.jku.at/phlo/pycli"

import os
import pkgutil
import sys

def run (path: str, main: str = "main"):
    module = pkgutil.resolve_name(path)
    cmd = os.path.basename(sys.argv[0])
    argv = []
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        try:
            module = pkgutil.resolve_name(path + f".{arg}")
            path += f".{arg}"
            cmd += f" {arg}"
        except Exception:
            argv = sys.argv[i:]
            break
    sys.argv = [cmd] + argv
    try:
        return getattr(module, main)()
    except AttributeError as e:
        print(f"usage: {cmd} <command> [<args>]\n\n{module.__doc__.strip()}\n")
        print("available commands:")
        cmds = []
        for m in pkgutil.iter_modules(module.__path__):
            doc = pkgutil.resolve_name(path + f".{m.name}").__doc__
            if doc: doc = doc.strip().split('\n', 1)[0]
            cmds.append((m.name, doc))
        spacing = 4
        width = (max([len(x[0]) for x in cmds]) + spacing + 1) // 2 * 2
        for name, doc in cmds:
            print(f"  {name:<{width}}{doc}")
        print()
        exit(1)

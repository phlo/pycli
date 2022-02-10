"""Modularized command line tools made easy."""

import os
import pkgutil
import sys

def run ():
    app = os.path.basename(sys.argv[0])
    margs = []
    mpath = __name__
    module = pkgutil.resolve_name(__name__)
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        try:
            module = pkgutil.resolve_name(mpath + f".{arg}")
            app += f" {arg}"
            mpath += f".{arg}"
        except Exception:
            margs = sys.argv[i:]
            break
    sys.argv = [app] + margs
    try:
        return getattr(module, "main")()
    except AttributeError as e:
        print(f"usage: {app} <command> [<args>]\n\n{module.__doc__}\n")
        print("available commands:")
        cmds = []
        for minfo in pkgutil.iter_modules(module.__path__):
            doc = pkgutil.resolve_name(mpath + f".{minfo.name}").__doc__
            if doc: doc = doc.split('\n', 1)[0]
            cmds.append((minfo.name, doc))
        nlen = max([len(x[0]) for x in cmds])
        nsep = 4 # seperator width
        nwidth = (nlen + nsep + 1) // 2 * 2
        for name, doc in cmds:
            print(f"  {name:<{nwidth}}{doc}")
        exit(1)

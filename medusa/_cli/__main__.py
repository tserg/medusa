import importlib
import sys
import traceback
from pathlib import Path

from medusa._config import __version__
from medusa.utils.docopt import docopt, levenshtein_norm

__doc__ = """Usage: medusa <command> [<args>...] [options <args>]

Commands:
  transform             Print the Vyper AST to console.
  analyse               Analyse Vyper code.

Options:
  --help -h             Display this message.
  --version             Show version and exit.
"""


def main():

    print(f"Medusa v{__version__} - Analyse Vyper code\n")

    if "--version" in sys.argv:
        sys.exit()

    if len(sys.argv) < 2 or sys.argv[1].startswith("-"):
        # this call triggers a SystemExit
        docopt(__doc__, ["medusa", "-h"])

    if "-i" in sys.argv:
        # a small kindness to ipython users
        sys.argv[sys.argv.index("-i")] = "-I"

    cmd = sys.argv[1]
    cmd_list = [i.stem for i in Path(__file__).parent.glob("[!_]*.py")]
    if cmd not in cmd_list:
        distances = sorted([(i, levenshtein_norm(cmd, i)) for i in cmd_list], key=lambda k: k[1])
        if distances[0][1] <= 0.2:
            sys.exit(f"Invalid command. Did you mean 'medusa {distances[0][0]}'?")
        sys.exit("Invalid command. Try 'medusa --help' for available commands.")

    sys.tracebacklimit = 1000

    try:
        sys.exit(importlib.import_module(f"medusa._cli.{cmd}").main())
    except Exception as e:
        tb_item = sys.exc_info()[2]
        traceback.print_tb(tb_item)
        print(e)

from medusa.analysis.analyse import analyse
from medusa.utils.docopt import docopt
from medusa.utils.output import format_analysis, write_analysis
from medusa.vyper.vyper_compile import get_vyper_ast

__doc__ = """Usage: medusa analyse [<contract>] [options]

Arguments
  [<contract>]          Name of Vyper contract to compile and analyse.

Options:
  --help -h             Display this message.
  --output <file>       Write the analysis to a file.
  --print-output        Print the analysis to console.

Analyses the Vyper source file
"""


def main():
    args = docopt(__doc__)

    if args["<contract>"]:
        path = args["<contract>"]
        print_output = args["--print-output"]

        # Get Vyper AST
        vyper_ast = get_vyper_ast(path)

        # Perform analysis and format the result as a string
        output_dict = analyse(vyper_ast)
        formatted_analysis = format_analysis(output_dict)

        # Write to output file
        output_file = args["--output"]
        if output_file:
            write_analysis(formatted_analysis, output_file)

        # Print analysis to console
        if print_output:
            print(formatted_analysis)

        print(f"\nSuccessfully analysed {path}!")

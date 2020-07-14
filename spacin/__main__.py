"""This is Spacin entrypoint!"""


import sys
import argparse
import textwrap

from spacin.spacin import Spacin
from spacin.algorithm import BasicAlgorithm


def main(args=None):
    """Project entrypoint function"""

    argparser = argparse.ArgumentParser(
        description="""Spacin, puts space in!""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            u"""developed by Mohammad Salek with \u2764

            """
        ),
        prog='spacin',
        usage="""%(prog)s <string>"""
    )

    argparser.add_argument(
        'input_str',
        action='store',
        type=str,
        nargs="?",
        help=argparse.SUPPRESS,
    )

    argparser.add_argument(
        '-t',
        '--text',
        action='store',
        metavar='<string>',
        type=str,
        help='accepts string text in commandline',
    )

    argparser.add_argument(
        '-a',
        '--algorithm',
        action='store',
        metavar='<algorithm name>',
        type=str,
        help='run with selected algorithm',
    )

    args = argparser.parse_args()
    if not any([args.input_str, args.text]):
        argparser.print_help()
        sys.exit(1)
    elif all([args.input_str, args.text]):
        argparser.print_help()
        sys.exit(1)
    else:
        input_str = args.input_str if args.input_str else args.text
        algo = BasicAlgorithm()
        print(f"algorithm:\t{algo}\ninput:\t{input_str}")
        print("processing...", end=' ')
        res = Spacin.run(algo, input_str)
        print("done!\n")
        print(f"as a sentence:\t\"{' '.join(res)}\"")
        print(f"as a list:\t{res}")

if __name__ == "__main__":
    main()

"""This is Spacin entrypoint"""


import sys
import argparse
import textwrap
import time

from spacin.spacin import Spacin
from spacin.algorithm import BasicAlgorithm


def main(args=None):
    """Project entrypoint function"""

    argparser = argparse.ArgumentParser(
        description="""\r\tSpacin, puts space in!\n\n
        \rSpacin is a word-separator that distinguishes
        \reach word in a given string.\n
        \rexample:
        \r> spacin "hellofriend"
        \r...
        \ras a sentence:    "hello friend"
        \ras a list:        ['hello', 'friend']
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """developed by Mohammad Salek
            \r\n
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
        help='accept input text in commandline',
    )

    argparser.add_argument(
        '-w',
        '--words',
        action='store_true',
        help='output result as words (as a list)')

    argparser.add_argument(
        '-s',
        '--sentence',
        action='store_true',
        help='output result in a sentence (as string)')

    try:
        args = argparser.parse_args()
        if not any([args.input_str, args.text]):
            argparser.print_help()
            sys.exit(1)
        elif all([args.input_str, args.text]):
            argparser.print_help()
            sys.exit(1)
        else:
            # show process details:
            show_process = True
            show_process = not any([args.sentence, args.words])
            # select input:
            input_str = args.input_str if args.input_str else args.text
            # choose algorithm(s):
            algo = BasicAlgorithm()
            # algorithm(s) and input details:
            if show_process:
                print(f"input text:\t{input_str}")
                print(f"algorithm:\t{algo}")
                print("processing...", end=' ', flush=True)
            # run algorithm(s):
            start_time = time.time()
            res = Spacin.run(algo, input_str)
            end_time = time.time()
            # yell finished:
            if show_process:
                print("done!")
                print(f"and it took {end_time-start_time:.3f} seconds\n")
            # show results:
            if not any([args.sentence, args.words]):
                print(f"as a sentence:\t\t\"{' '.join(res)}\"")
                print(f"as separate words:\t{res}")
            elif all([args.sentence, args.words]):
                print(f"\"{' '.join(res)}\"")
                print(f"{res}")
            elif args.sentence:
                print(f"\"{' '.join(res)}\"")
            elif args.words:
                print(f"{res}")

    except argparse.ArgumentTypeError as arge:
        print('\n\nan argument error occured:', arge)
        print('enter "spacin -h" for help')
        sys.exit(1)


if __name__ == "__main__":
    main()

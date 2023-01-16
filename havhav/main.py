import argparse
import sys

from typing import Optional, Sequence

from .handler import get_dog_facts


def main(argv: Optional[Sequence[str]] = None) -> int:
    """
    Main function for CLI functionality

    :param argv: CLI arguments
    :return: Return code
    :rtype: int
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("nof", help="number of facts", nargs="?", default=1)
    args = parser.parse_args(argv)

    try:
        hav = int(args.nof)
        facts = get_dog_facts(number_of_facts=hav)
        for fact in facts:
            print(fact)
    except Exception:
        print("havhav number of facts must be an integer!", file=sys.stderr)
        return 1
    return 0

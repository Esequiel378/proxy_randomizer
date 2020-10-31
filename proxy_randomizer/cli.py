"""Command line for proxy_randomizer."""

# built in modules
import argparse
import sys

# local modules
from proxy_randomizer.providers import RegisteredProviders

# third party modules

# type hint


def main() -> None:
    """Console script for proxy_randomizer."""

    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    parser

    # create a RegisteredProviders instance
    rp = RegisteredProviders()
    # parse providers
    rp.parse_providers()

    # log out a random proxy
    print(rp.get_random_proxy())

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

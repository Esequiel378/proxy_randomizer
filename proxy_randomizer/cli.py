"""Console script for proxy_randomizer."""

# built in modules
# ---------------------------------------------------------------
import argparse
import sys

# local modules
# ---------------------------------------------------------------
from proxy_randomizer.providers import RegisteredProviders

# third party modules
# ---------------------------------------------------------------

# type hint
# ---------------------------------------------------------------



def main() -> None:
    """Console script for proxy_randomizer."""

    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    # create a RegisteredProviders instance
    p = RegisteredProviders()
    # parse providers
    p.parse_providers()

    # log out a random proxy
    print(f"proxy: {p.get_random_proxy()}")

    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

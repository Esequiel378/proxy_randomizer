# built in modules
# ---------------------------------------------------------------
import random

# local modules
# ---------------------------------------------------------------
from proxy_randomizer.providers import Provider
from proxy_randomizer.proxy     import Proxy

# third party modules
# ---------------------------------------------------------------

# type hint
# ---------------------------------------------------------------
from typing import List, Optional, Callable

# ProxyList
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ProxyList:

    # __init__
    # ---------------------------------------------------------------
    def __init__(self, providers : List[Provider]):
        
        self.proxies    : List[Proxy]       = list()
        self._providers : List[Provider]    = providers

    # parse_providers
    # ---------------------------------------------------------------
    def parse_providers(self):

        for provider in self._providers:

            # parse provider
            provider.parse()
            # get proxies
            self.proxies.extend(provider.proxies)
            # delete provider
            del provider.proxies

    # get_random_proxy
    # ---------------------------------------------------------------
    def get_random_proxy(self, predicate : Optional[Callable] = None):

        if not predicate is None:

            return random.choice(
                filter(predicate, self.proxies)
            )

        return random.choice(self.proxies)
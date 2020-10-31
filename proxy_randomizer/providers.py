"""Provider module to handle all providers related stuff"""

# built in modules
import random

# local modules
from proxy_randomizer.proxy import Proxy, Anonymity
from proxy_randomizer import utils

# third party modules
import requests
from bs4 import BeautifulSoup

# type hint
from typing import List, Optional, Callable
from proxy_randomizer.proxy import Proxy


class Provider:
    """Provider."""

    def __init__(self, url: str, attrs: dict):
        """Provider contructor.

        :param  url     : proxy provider url
        :type   url     : str

        :param  attrs   : attributes to find table in html
        :type   attrs   : dict
        """

        self.url: str = url
        self.attrs: dict = attrs
        self.proxies: list = list()

    def parse(self) -> None:
        """parse proxies from providers page.

        :raises Exception: error while geting provider page
        """

        # get provider page
        response = requests.get(self.url, timeout=5)

        # check for error on response
        if response.status_code != 200:
            raise Exception(f"reponse error {response.status_code}")

        # parse provider proxies table
        parsed_table = utils.get_table_content(response.text, attrs=self.attrs)

        # create and store proxies
        self.proxies = [
            Proxy(
                ip_address=elm.get("ip address"),
                port=elm.get("port"),
                country=elm.get("country"),
                anonymity=utils.get_anonymity_level(elm.get("anonymity")),
            )
            for elm in parsed_table
        ]


class RegisteredProviders:
    """RegisteredProviders."""

    def __init__(self, disable_defaults: bool = False) -> None:
        """RegisteredProviders contructor.

        :param  disable_defaults: disable default providers, defaults to False
        :type   disable_defaults: bool, optional
        """

        self.proxies: List[Proxy] = list()

        self.__registered_providers: List[Provider] = []

        if not disable_defaults:
            FreeProxyProvider = Provider(
                "https://free-proxy-list.net/", attrs={"id": "proxylisttable"}
            )
            SslProxyProvider = Provider(
                "https://www.sslproxies.org/", attrs={"id": "proxylisttable"}
            )
            # PremProxyProvider   : Provider  = Provider  ("https://premproxy.com/list/"  , attrs={"id":"proxylistt"})

            # register defaults providers
            list(
                map(self.register_provider, [FreeProxyProvider, SslProxyProvider])
            )  # PremProxyProvider

    def register_provider(self, provider: Provider, run_parser: bool = False) -> None:
        """register a new provider.

        :param  provider    : provider to register
        :type   provider    : Provider

        :param  run_parser  : determine if provider must be parsed before it's register, defaults to True
        :type   run_parser  : bool, optional

        :raises Exception   : inherence from Provider.parse method
        """

        # parse provider
        if run_parser:
            provider.parse()

        # register provider
        self.__registered_providers.append(provider)

    def get_registered_providers(self) -> List[Provider]:
        """return a list of stored providers.

        :return : List of providers
        :rtype  : List[Provider]
        """

        return self.__registered_providers

    def parse_providers(self) -> None:
        """parse all stored providers."""

        # iterate thorugh registerd providers
        for provider in self.__registered_providers:
            # parse provider
            provider.parse()
            # get and store proxies
            self.proxies.extend(provider.proxies)
            # delete provider proxies to save memory
            del provider.proxies

    def get_random_proxy(self, predicate: Optional[Callable] = None) -> Proxy:
        """get a random stored proxy.

        :param  predicate   : optional function to run a filter before get a random choice, defaults to None
        :type   predicate   : Optional[Callable], optional

        :return             : random proxy
        :rtype              : Proxy
        """

        # proxies
        proxies = self.proxies

        # chec if predicate must be executed and run filter
        if not predicate is None:
            proxies = filter(predicate, self.proxies)

        # return random choice
        return random.choice(proxies)

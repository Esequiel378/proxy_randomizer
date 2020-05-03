# built in modules
# ---------------------------------------------------------------

# local modules
# ---------------------------------------------------------------
from proxy_randomizer.proxy import Proxy, Anonymity
from proxy_randomizer import utils

# third party modules
# ---------------------------------------------------------------
import requests
from bs4 import BeautifulSoup

# type hint
# ---------------------------------------------------------------
from typing import List



# Provider
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Provider:

    # __init__
    # ---------------------------------------------------------------
    def __init__(self, url, attrs):

        self.url        : str   = url
        self.proxies    : list  = list()
        self.attrs      : dict  = attrs

    # parse
    # ---------------------------------------------------------------
    def parse(self):

        response = requests.get(self.url, timeout=5)

        if response.status_code != 200: raise Exception(f"reponse error {response.status_code}")

        with open("t.html", "w") as f:
            f.write(response.text)
        
        parsed_table = utils.get_table_content(response.text, attrs=self.attrs)

        self.proxies = [ Proxy(

            ip_address  = elm.get("ip address"),
            port        = elm.get("port"),
            country     = elm.get("country"),
            anonymity   = utils.get_anonymity_level(elm.get("anonymity")),

        ) for elm in parsed_table ]


# Providers instances
# ---------------------------------------------------------------
FreeProxyProvider   : Provider  = Provider("https://free-proxy-list.net/" , attrs={"id":"proxylisttable"})
SslProxyProvider    : Provider  = Provider("https://www.sslproxies.org/"  , attrs={"id":"proxylisttable"})

# TODO: porst are loaded from js, handle this asap
# PremProxyProvider   : Provider  = Provider  ("https://premproxy.com/list/"  , attrs={"id":"proxylistt"})

ALL_PROVIDERS : List[Provider]  = [
    FreeProxyProvider,
    SslProxyProvider,
    # PremProxyProvider,
]

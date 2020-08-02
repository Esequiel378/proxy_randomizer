"""Proxy module to handle all proxies related stuff"""

# built in modules
# ---------------------------------------------------------------

# local modules
# ---------------------------------------------------------------

# third party modules
# ---------------------------------------------------------------

# type hint
# ---------------------------------------------------------------
import typing as t


# Anonymity
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Anonymity:
    """Anonymity.

    ...
    Attributes
    ----------

    level: int
        integer that assign a level for anonimity

    name: str
        a representative name for Anonimity

    ...
    Methods
    -------

    __str__() -> str
        return a string representation of anonymity
    """

    # __init__
    # ---------------------------------------------------------------
    def __init__(self, name : str, level : int):
        """Anonymity constructor.

        :param  name    : a representative name for Anonimity
        :type   name    : str

        :param  level   : integer that assign a level for anonimity
        :type   level   : int
        """

        self.name   : str = name
        self.level  : int = level

    # __repr__
    # ---------------------------------------------------------------
    def __repr__(self) -> str:

        """return a string representation of anonymity.

        :return : string representation
        :rtype  : str
        """

        return f"Anonimity(name='{self.name}, level={self.level}')"

    # __str__
    # ---------------------------------------------------------------
    def __str__(self) -> str:
        """return a string representation of anonymity.

        :return : string representation
        :rtype  : str
        """

        return f"{self.name} {self.level}"



# Proxy
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Proxy:
    """Proxy.

    ...
    Attributes
    ----------

    ip_address: str
        proxy ip address

    port: t.Union[int, str]
        proxy port

    country: str
        proxy country

    anonymity: Anonymity
        proxy anonymity
    """

    # __init__
    # ---------------------------------------------------------------
    def __init__(self, ip_address : str, port : t.Union[int, str], country : str, anonymity : Anonymity) -> None:
        """Proxy contrunctor.

        :param  ip_address  : proxy ip address
        :type   ip_address  : str

        :param  port        : proxy port
        :type   port        : t.Union[int, str]

        :param  country     : proxy country
        :type   country     : str

        :param  anonymity   : proxy anonymity
        :type   anonymity   : Anonymity
        """

        self.ip_address : str       = ip_address
        self.port       : int       = port

        self.country    : str       = country
        self.anonymity  : Anonymity = anonymity

    # __str__
    # ---------------------------------------------------------------
    def __str__(self) -> str:
        """return a string representation of Proxy.

        :return : proxy string representation
        :rtype  : str
        """

        return f"{self.get_proxy()} {self.country} {self.anonymity.__str__()}"

    # get_proxy
    # ---------------------------------------------------------------
    def get_proxy(self) -> str:
        """formated url:port string.

        :return : url:port string
        :rtype  : str
        """

        return f"{self.ip_address}:{self.port}"

"""Proxy module to handle all proxies related stuff"""

# built in modules
from enum import Enum

# local modules

# third party modules

# type hint
import typing as t


class Anonymity(bytes, Enum):
    """Anonymity."""

    def __new__(cls, value: int, label: str, description: str):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        obj.description = description

        return obj

    UNKNOWN = (0, "Unknown", "Unknown anonymity level.")
    ELITE = (1, "Elite", "Provide the very highest level of anonymity.")
    ANONYMOUS = (
        2,
        "Anonymous",
        "Provide a degree of anonymity acceptable for many purposes.",
    )
    TRANSPARENT = (
        3,
        "Transparent",
        "Do not hide your IP address from a server you are connecting to, so it does not provide anonymity.",
    )


class Proxy:
    """Proxy."""

    def __init__(
        self,
        ip_address: str,
        port: t.Union[int, str],
        country: str,
        anonymity: Anonymity,
    ) -> None:
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

        self.ip_address: str = ip_address
        self.port: int = port

        self.country: str = country
        self.anonymity: Anonymity = anonymity

    def __str__(self) -> str:
        """return a string representation of Proxy.

        :return : proxy string representation
        :rtype  : str
        """

        return f"{self.get_proxy()} {self.country} {self.anonymity.label}"

    def get_proxy(self) -> str:
        """formated url:port string.

        :return : url:port string
        :rtype  : str
        """

        return f"{self.ip_address}:{self.port}"

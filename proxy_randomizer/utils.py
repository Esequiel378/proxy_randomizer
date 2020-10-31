"""utils to consume from modules"""

# built in modules
import unicodedata

# local modules
from proxy_randomizer.proxy import Anonymity

# third party modules
import requests
from bs4 import BeautifulSoup

# type hint
from typing import Optional, List, Dict


class NotFoundError(Exception):
    pass


# Anonymity constants as list to run within a filter
ANONYMITY_LEVELS = [
    Anonymity.UNKNOWN,
    Anonymity.ELITE,
    Anonymity.ANONYMOUS,
    Anonymity.TRANSPARENT,
]


def remove_accents(string: str) -> str:
    """Remove wired characters from string"""

    return "".join(
        c for c in unicodedata.normalize("NFKD", string) if not unicodedata.combining(c)
    )


def contains(container: str, string: str) -> bool:
    """Check if container string contains a given string."""

    container = remove_accents(container).lower()
    string = remove_accents(string).lower()

    return string in container


def get_anonymity_level(anonymity: Optional[str] = None) -> Anonymity:
    """return the anonymity level from a given string.

    :param  anonymity   : anonymity name, default None
    :type   anonymity   : Optional[str]

    :return             : Anonymity instance
    :rtype              : Anonymity
    """

    # if not anonymity is given, return unknown
    if not anonymity:
        return Anonymity.UNKNOWN

    # predicate to find anonnymity instance
    predicate = lambda anonymity_level: contains(anonymity, anonymity_level.label)

    # find and return anonymity instance or UNKNOWN if can not find any
    anonymity_level = (
        next(filter(predicate, ANONYMITY_LEVELS), None) or Anonymity.UNKNOWN
    )

    return anonymity_level


def get_table_content(html: str, attrs: dict) -> List[Dict[str, str]]:
    """Get all elementes from a table and return a key-pair list.

    :param  html            : html content where table must be scraped
    :type   html            : str

    :param  attrs           : attributes to find the table
    :type   attrs           : dict

    :raises NotFoundError   : raise error if table can not be found

    :return                 : list of objects where each list items is a row in the table, as object, where the column header is the key, and the column value as the object value
    :rtype                  : List[Dict[str, str]]
    """

    # parse response
    soup = BeautifulSoup(html, "lxml")

    # find table
    table = soup.find("table", attrs)

    # if table can not be found, raise NotFoundError
    if table is None:
        raise NotFoundError(f"table {attrs} does not exist")

    # get table headers
    headers = [th.text.lower() for th in soup.find("thead").find("tr").find_all("th")]

    # parse and return table content, row by row
    table_content = [
        {header: td.text for header, td in zip(headers, tr.find_all("td"))}
        for tr in table.find("tbody").find_all("tr")
    ]

    return table_content

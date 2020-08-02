"""utils to consume from modules"""

# built in modules
# ---------------------------------------------------------------

# local modules
# ---------------------------------------------------------------
from proxy_randomizer.proxy import Anonymity

# third party modules
# ---------------------------------------------------------------
import requests
from bs4 import BeautifulSoup

# type hint
# ---------------------------------------------------------------
import typing as t



# NotFoundError
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NotFoundError(Exception):
   pass



# Anonymities constants
UNKNOWN         = Anonymity(level=4, name="UNKNOWN")      # type: t.Final
TRANSPARENT     = Anonymity(level=3, name="TRANSPARENT")  # type: t.Final
ANONYMOUS       = Anonymity(level=2, name="ANONYMOUS")    # type: t.Final
ELITE           = Anonymity(level=1, name="ELITE")        # type: t.Final



# Anonymity constants as list to run within a filter
ANONYMITY_LEVELS = [UNKNOWN, TRANSPARENT, ANONYMOUS, ELITE]



# get_anonymity_level
# ---------------------------------------------------------------
def get_anonymity_level(anonymity: t.Optional[str] = None) -> Anonymity:
    """return an anonymity instance from a given string.

    :param  anonymity   : anonymity name, default None
    :type   anonymity   : t.Optional[str]

    :return             : Anonymity instance
    :rtype              : Anonymity
    """

    # if not anonymity is given, return unknown
    if not anonymity: return UNKNOWN

    # predicate to find anonnymity instance
    predicate = lambda anonymity_level: anonymity.lower() in anonymity_level.name.lower()

    # find and return anonymity instance or UNKNOWN if can not find any
    return next( filter(predicate, ANONYMITY_LEVELS), None ) or UNKNOWN



# get_table_content
# ---------------------------------------------------------------
def get_table_content(html : str, attrs : dict) -> t.List[t.Dict[str, str]]:
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
    if table is None: raise NotFoundError(f"table {attrs} does not exist")

    # get table headers
    headers = [ th.text.lower() for th in soup.find("thead").find("tr").find_all("th") ]

    # parse and return table content, row by row
    return [{

        header : td.text for header, td in zip(headers, tr.find_all("td"))

    } for tr in table.find("tbody").find_all("tr") ]


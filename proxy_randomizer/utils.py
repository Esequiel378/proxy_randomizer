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
from typing import List, Dict, Final

# NotFoundError
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NotFoundError(Exception):
    pass

UNKNOWN     : Final     = Anonymity(level=0, name="UNKNOWN")
TRANSPARENT : Final     = Anonymity(level=1, name="TRANSPARENT")
ANONYMOUS   : Final     = Anonymity(level=2, name="ANONYMOUS")
ELITE       : Final     = Anonymity(level=3, name="ELITE")

ANONYMITY_LEVELS = {
    "unknown"       : UNKNOWN,
    "transparent"   : TRANSPARENT,
    "anonymous"     : ANONYMOUS,
    "elite"         : ELITE,
}

def get_anonymity_level(anonymity : str) -> Anonymity:

    if not anonymity: return UNKNOWN

    return [ 
        
        value for key, value in ANONYMITY_LEVELS.items() 
        if key in anonymity.lower() 

    ][0] or UNKNOWN

def get_table_content(html : str, attrs : dict) -> List[Dict[str, str]]:
    """Get all elementes from a table and return a key-pair list"""

    # parse response
    soup = BeautifulSoup(html, "lxml")

    # find table
    table = soup.find("table", attrs)

    if table is None: raise NotFoundError(f"table {attrs} does not exist")

    headers = [ th.text.lower() for th in soup.find("thead").find("tr").find_all("th") ]

    return [{

        header : td.text for header, td in zip(headers, tr.find_all("td"))

    } for tr in table.find("tbody").find_all("tr") ]


# built in modules
# ---------------------------------------------------------------

# local modules
# ---------------------------------------------------------------

# third party modules
# ---------------------------------------------------------------

# type hint
# ---------------------------------------------------------------



# Anonymity
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Anonymity:
    
    # __init__
    # ---------------------------------------------------------------
    def __init__(self, level : int, name : str):

        self.level  : int = level
        self.name   : str = name

    # __str__
    # ---------------------------------------------------------------
    def __str__(self) -> str:
        return f"{self.name} {self.level}"

# Proxy
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Proxy:

    # __init__
    # ---------------------------------------------------------------
    def __init__(self, ip_address : str, port : int, country : str, anonymity : Anonymity) -> None:

        self.ip_address : str       = ip_address
        self.port       : int       = port

        self.country    : str       = country
        self.anonymity  : Anonymity = anonymity

    # __str__
    # ---------------------------------------------------------------
    def __str__(self) -> str:
        return f"{self.get_proxy()} {self.country} {self.anonymity}"

    # get_proxy
    # ---------------------------------------------------------------
    def get_proxy(self) -> str:
        return f"{self.ip_address}:{self.port}"
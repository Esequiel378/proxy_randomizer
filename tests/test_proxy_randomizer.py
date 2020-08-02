#!/usr/bin/env python

"""Tests for `proxy_randomizer` package."""

# built in modules
# ---------------------------------------------------------------
import json
from pathlib import Path

# local modules
# ---------------------------------------------------------------
from proxy_randomizer import proxy, utils

# third party modules
# ---------------------------------------------------------------
import pytest

# type hint
# ---------------------------------------------------------------


# TestProxy
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TestProxy:

    # test_anonymity
    # ---------------------------------------------------------------
    def test_anonymity(self):

        a = proxy.Anonymity(level=3, name="ELITE")

        assert a.__str__() == "ELITE 3"

    # test_proxy
    # ---------------------------------------------------------------
    def test_proxy(self):

        p = proxy.Proxy(
            ip_address  = "127.0.0.1",
            port        = "8000",
            country     = "Argentina",
            anonymity   = utils.UNKNOWN
        )

        assert p.__str__() == "127.0.0.1:8000 Argentina UNKNOWN 4"
        assert p.get_proxy() == "127.0.0.1:8000"




FILES_PATH = Path(__file__).parents[1] / "tests/files"



# TestUtils
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TestUtils:

    # test_get_anonymity_level
    # ---------------------------------------------------------------
    def test_get_anonymity_level(self):

        anonymity = utils.get_anonymity_level("transparent")

        assert anonymity == utils.TRANSPARENT

    # test_bad_get_anonymity_level
    # ---------------------------------------------------------------
    def test_bad_get_anonymity_level(self):

        anonymity = utils.get_anonymity_level("")
        assert anonymity == utils.UNKNOWN

    # test_get_table_content
    # ---------------------------------------------------------------
    def test_get_table_content(self, tmpdir):

        input_file  = FILES_PATH / "get_table_content/table_content.html"
        output_file = FILES_PATH / "get_table_content/output.json"

        with open(input_file.as_posix(), "r") as f:

            parsed_data = utils.get_table_content(
                f.read(), attrs={"id":"proxylisttable"}
            )

            with open(output_file.as_posix(), "r") as of:
                assert parsed_data == json.loads( of.read() )

    # test_bad_get_table_content
    # ---------------------------------------------------------------
    def test_bad_get_table_content(self):

        with pytest.raises(utils.NotFoundError):
            utils.get_table_content("", attrs=dict())


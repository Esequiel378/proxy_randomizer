================
proxy-randomizer
================


.. image:: https://img.shields.io/pypi/v/proxy_randomizer.svg?version=latest
        :target: https://pypi.python.org/pypi/proxy_randomizer

.. image:: https://travis-ci.com/Esequiel378/proxy_randomizer.svg?branch=master
        :target: https://travis-ci.com/Esequiel378/proxy_randomizer

.. image:: https://readthedocs.org/projects/proxy-randomizer/badge/?version=latest
        :target: https://proxy-randomizer.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://static.pepy.tech/personalized-badge/proxy-randomizer?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads
        :target: https://pepy.tech/project/proxy-randomizer
        :alt: Total Downloads

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/psf/black
        :alt: Black Formater


proxy randomizer


* Free software: MIT license
* Documentation: https://proxy-randomizer.readthedocs.io.


Description
------------------

Inpired by `http-request-randomizer`_

proxy_randomizer is intended to use for small-meduim web scrapers/crawlers, helping to avoid
temporal/permanent bans from web pages, generating random proxies to include in the requests


Installation
------------

.. code-block:: python

   pip install proxy_randomizer


API
---

To use proxy_randomizer in your code, you just need to generate a
RegisteredProviders instance and parse the providers.

.. code-block:: python

    from proxy_randomizer import RegisteredProviders

    rp = RegisteredProviders()
    rp.parse_providers()

    print(f"proxy: {rp.get_random_proxy()}")


You can iterate throughout all proxies as simple as this.

.. code-block:: python

   from proxy_randomizer import RegisteredProviders
   import requests

   rp = RegisteredProviders()
   rp.parse_providers()

   for proxy in rp.proxies:

        proxies     = {"https": proxy.get_proxy()}
        response    = requests.get("http://google.com", proxies=proxies)


If you need to hide your identity, you can filter the proxy list by its
anonymity level.

.. code-block:: python

   from proxy_randomizer import RegisteredProviders
   from proxy_randomizer.proxy import Anonymity

   rp = RegisteredProviders()
   rp.parse_providers()

   anonymous_proxies = list(
       filter(lambda proxy: proxy.anonymity == Anonymity.ANONYMOUS, rp.proxies)
   )

   print(f"filtered proxies: {anonymous_proxies}")


There are four different anonymity levels, you can inspect them like this

.. code-block:: python

   from proxy_randomizer.utils import ANONYMITY_LEVELS

   for level in ANONYMITY_LEVELS:
      print(level.label)


Command-line interface
----------------------

If you need some quick proxy, just type this in your terminal.

.. code-block:: bash

   proxy_randomizer


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`http-request-randomizer`: https://github.com/pgaref/HTTP_Request_Randomizer

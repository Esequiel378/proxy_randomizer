#!/usr/bin/env python

"""Tests for `providers` module."""

# built in modules

# local modules
from proxy_randomizer.providers import Provider, RegisteredProviders
from proxy_randomizer.proxy import Proxy

# third party modules

# type hint


class TestProvider:
    def test_provider_constructor(self):
        """check provider constructor and attributes types"""

        url = "https://test-provider.net/"
        attrs = {"id": "proxylisttable"}

        provider_instance = Provider(url=url, attrs=attrs)

        assert provider_instance.url == url
        assert provider_instance.attrs == attrs
        assert isinstance(provider_instance.proxies, list) == True

    def test_freeproxy_provider(self):

        url = "https://free-proxy-list.net/"
        attrs = {"id": "proxylisttable"}

        provider_instance = Provider(url=url, attrs=attrs)

        provider_instance.parse()

        assert isinstance(provider_instance.proxies[0], Proxy)

    def test_sslproxy_provider(self):

        url = "https://www.sslproxies.org/"
        attrs = {"id": "proxylisttable"}

        provider_instance = Provider(url=url, attrs=attrs)

        provider_instance.parse()

        assert isinstance(provider_instance.proxies[0], Proxy)


class TestRegisteredProviders:
    def test_registered_providers_constructor_with_defaults_providers(self):

        r = RegisteredProviders(disable_defaults=False)

        print(r.get_registered_providers())

        assert len(r.get_registered_providers()) != 0
        assert isinstance(r.get_registered_providers()[0], Provider)

        assert isinstance(r.proxies, list)

    def test_registered_providers_constructor_without_defaults_providers(self):

        r = RegisteredProviders(disable_defaults=True)

        assert len(r.get_registered_providers()) == 0
        assert isinstance(r.proxies, list)

    def test_registered_providers_parse_providers(self):

        r = RegisteredProviders(disable_defaults=False)

        r.parse_providers()

        assert len(r.proxies) != 0
        assert isinstance(r.proxies[0], Proxy)

        assert hasattr(r, "proxies")

    def test_registered_get_random_proxy(self):

        url = "https://www.sslproxies.org/"
        attrs = {"id": "proxylisttable"}

        test_provider = Provider(url=url, attrs=attrs)

        r = RegisteredProviders(disable_defaults=True)
        r.register_provider(test_provider)

        r.parse_providers()

        rand_proxy = r.get_random_proxy()

        assert isinstance(rand_proxy, Proxy)

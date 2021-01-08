#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests>=2.23.0',
    'beautifulsoup4>=4.9.0',
    'lxml>=4.5.0',
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Esequiel Albornoz",
    author_email='esequielalbornoz7@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="proxy randomizer",
    entry_points={
        'console_scripts': [
            'proxy_randomizer=proxy_randomizer.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='proxy_randomizer',
    name='proxy_randomizer',
    packages=find_packages(include=['proxy_randomizer', 'proxy_randomizer.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/esequiel378/proxy_randomizer',
    version='1.3.0',
    zip_safe=False,
)

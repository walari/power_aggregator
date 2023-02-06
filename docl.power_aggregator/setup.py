# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from setuptools import setup

setup(
    name="docl.power_aggregator",
    version="0.1.0",
    description="Solar power plant aggregator",
    author="Clément Dolou",
    author_email="",
    packages=find_packages(),
    install_requires=[
        "requests",
        "argparse",
        "PyYAML"
    ],
    license="")
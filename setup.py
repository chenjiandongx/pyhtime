#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
    name="pytimeago",
    version="0.0.1",
    author="chenjiandongx",
    description="一个用来将 datetime 时间转化成更加人性化的`时间描述字符串`",
    url="https://github.com/chenjiandongx/pytiemago",
    author_email="chenjiandongx@qq.com",
    license="MIT",
    py_modules=["pytimeago"],
    install_requires=["moment"],
)

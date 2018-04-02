#!/usr/bin/env python
# coding=utf-8

import datetime

from pyhtime import htime


def test_just_now():
    assert htime(datetime.datetime.now()) == "刚刚"
    assert htime(datetime.datetime.now(), local="en") == "just now"


def test_second():
    d1 = datetime.datetime(2018, 8, 8, 0, 0, 1)
    d2 = datetime.datetime(2018, 8, 8, 0, 0, 2)
    d3 = datetime.datetime(2018, 8, 8, 0, 0, 3)
    assert htime(d1, d2) == "1 秒前"
    assert htime(d1, d2, local="en") == "1 second ago"
    assert htime(d1, d3, local="en") == "2 seconds ago"
    assert htime(d2, d1) == "1 秒后"
    assert htime(d2, d1, local="en") == "1 second later"
    assert htime(d3, d1, local="en") == "2 seconds later"


def test_minute():
    d1 = datetime.datetime(2018, 8, 8, 0, 1, 0)
    d2 = datetime.datetime(2018, 8, 8, 0, 2, 0)
    d3 = datetime.datetime(2018, 8, 8, 0, 3, 0)
    assert htime(d1, d2) == "1 分钟前"
    assert htime(d1, d2, local="en") == "1 minute ago"
    assert htime(d1, d3, local="en") == "2 minutes ago"
    assert htime(d2, d1) == "1 分钟后"
    assert htime(d2, d1, local="en") == "1 minute later"
    assert htime(d3, d1, local="en") == "2 minutes later"


def test_hour():
    d1 = datetime.datetime(2018, 8, 8, 1, 0, 0)
    d2 = datetime.datetime(2018, 8, 8, 2, 0, 0)
    d3 = datetime.datetime(2018, 8, 8, 3, 0, 0)
    assert htime(d1, d2) == "1 小时前"
    assert htime(d1, d2, local="en") == "1 hour ago"
    assert htime(d1, d3, local="en") == "2 hours ago"
    assert htime(d2, d1) == "1 小时后"
    assert htime(d2, d1, local="en") == "1 hour later"
    assert htime(d3, d1, local="en") == "2 hours later"


def test_day():
    d1 = datetime.datetime(2018, 8, 8, 0, 0, 0)
    d2 = datetime.datetime(2018, 8, 9, 0, 0, 0)
    d3 = datetime.datetime(2018, 8, 10, 0, 0, 0)
    assert htime(d1, d2) == "1 天前"
    assert htime(d1, d2, local="en") == "1 day ago"
    assert htime(d1, d3, local="en") == "2 days ago"
    assert htime(d2, d1) == "1 天后"
    assert htime(d2, d1, local="en") == "1 day later"
    assert htime(d3, d1, local="en") == "2 days later"


def test_month():
    d1 = datetime.datetime(2018, 8, 8, 0, 0, 0)
    d2 = datetime.datetime(2018, 9, 8, 0, 0, 0)
    d3 = datetime.datetime(2018, 10, 8, 0, 0, 0)
    assert htime(d1, d2) == "1 个月前"
    assert htime(d1, d2, local="en") == "1 month ago"
    assert htime(d1, d3, local="en") == "2 months ago"
    assert htime(d2, d1) == "1 个月后"
    assert htime(d2, d1, local="en") == "1 month later"
    assert htime(d3, d1, local="en") == "2 months later"


def test_year():
    d1 = datetime.datetime(2018, 8, 8, 0, 0, 0)
    d2 = datetime.datetime(2019, 8, 8, 0, 0, 0)
    d3 = datetime.datetime(2020, 8, 8, 0, 0)
    assert htime(d1, d2) == "1 年前"
    assert htime(d1, d2, local="en") == "1 year ago"
    assert htime(d1, d3, local="en") == "2 years ago"
    assert htime(d2, d1) == "1 年后"
    assert htime(d2, d1, local="en") == "1 year later"
    assert htime(d3, d1, local="en") == "2 years later"

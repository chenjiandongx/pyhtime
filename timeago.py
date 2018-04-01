#!/usr/bin/env python
# coding=utf-8

import datetime

import moment

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
MONTH = DAY * 31
YEAR = MONTH * 12


def timeago(when, base=None):
    """

    :param when:
    :param base:
    :return:
    """
    when = moment.date(when).datetime.timestamp()
    if not base:
        base = datetime.datetime.now()
    gone = base.timestamp() - when
    if gone < 0:
        return _translate(abs(gone), "后")
    else:
        return _translate(gone, "前")


def _get_format_humanize(num, unit, postfix):
    """

    :param num:
    :param unit:
    :param postfix:
    :return:
    """
    return "{} {}{}".format(int(num), unit, postfix)


def _translate(gone, postfix):
    """

    :param gone:
    :param postfix:
    :return:
    """
    if 0 < gone < 1:
        return "刚刚"
    elif 1 < gone < MINUTE:
        return _get_format_humanize(gone, "秒", postfix)
    elif MINUTE <= gone < HOUR:
        return _get_format_humanize(gone / MONTH, "分钟", postfix)
    elif HOUR <= gone < DAY:
        return _get_format_humanize(gone / HOUR, "小时", postfix)
    elif DAY < gone < MONTH:
        return _get_format_humanize(gone / DAY, "天", postfix)
    elif MONTH <= gone < YEAR:
        return _get_format_humanize(gone / MONTH, "月", postfix)
    elif gone >= YEAR:
        return _get_format_humanize(gone / YEAR, "年", postfix)

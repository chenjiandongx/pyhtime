#!/usr/bin/env python
# coding=utf-8

import datetime

import moment

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
MONTH = DAY * 30.4
YEAR = MONTH * 12


EN_UE = {
    "ago": "ago",
    "later": "later",
    "just_now": "just now",
    "second": "seconds",
    "minute": "minutes",
    "hour": "hours",
    "day": "days",
    "month": "months",
    "year": "years",
}

ZH_CN = {
    "ago": "前",
    "later": "后",
    "just_now": "刚刚",
    "second": "秒",
    "minute": "分钟",
    "hour": "小时",
    "day": "天",
    "month": "个月",
    "year": "年",
}


def htime(when, base=None, local="zh"):
    """
    主函数

    :param when: 想要转换的时间，可以为
        字符串格式："2018-4-1"
        英文时间："April 1, 2018"
        时间元组：(2018, 4, 1)
        datetime.datetime 类型：datetime.datetime(2018, 4, 1)
    :param base: 基准时间，默认为`datetime.datetime.now()`，类型同`when`
    :param local: 显示语言，默认为中文'zh',可选英文为'en'
    """
    when = moment.date(when).datetime.timestamp()

    if not base:
        _base = datetime.datetime.now().timestamp()
    else:
        _base = moment.date(base).datetime.timestamp()
    gone = _base - when
    if gone < 0:
        return _translate(abs(gone), local, "later")

    else:
        return _translate(gone, local, "ago")


def _get_format_humanize(num, unit, postfix):
    """
    返回更加人性化的 `时间描述字符串`

    :param num: 转换后的时间数字
    :param unit: 时间单位
    :param postfix: 时间后缀
    """
    if postfix in ("ago", "later"):
        if int(num) == 1:
            unit = unit[:-1]
        return "{} {} {}".format(int(num), unit, postfix)

    return "{} {}{}".format(int(num), unit, postfix)


def _translate(gone, local, postfix):
    """
    根据时间转换成更加人性化的 `时间描述字符串`

    :param gone: 根据时间戳计算的秒数
    :param local: 显示语言，默认为中文'zh',可选英文为'en'
    :param postfix: 时间后缀
    """
    local = ZH_CN if local == "zh" else EN_UE
    postfix = local.get(postfix)
    if 0 <= gone < 1:
        return local.get("just_now")

    elif 1 <= gone < MINUTE:
        return _get_format_humanize(gone, local.get("second"), postfix)

    elif MINUTE <= gone < HOUR:
        return _get_format_humanize(gone / MINUTE, local.get("minute"), postfix)

    elif HOUR <= gone < DAY:
        return _get_format_humanize(gone / HOUR, local.get("hour"), postfix)

    elif DAY <= gone < MONTH:
        return _get_format_humanize(gone / DAY, local.get("day"), postfix)

    elif MONTH <= gone < YEAR:
        return _get_format_humanize(gone / MONTH, local.get("month"), postfix)

    elif gone >= YEAR:
        return _get_format_humanize(gone / YEAR, local.get("year"), postfix)

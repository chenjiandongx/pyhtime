# pyhtime

[![Build Status](https://travis-ci.org/chenjiandongx/pyhtime.svg?branch=master)](https://travis-ci.org/chenjiandongx/pyhtime) [![Build status](https://ci.appveyor.com/api/projects/status/pbvuq6ejlmsbwc22/branch/master?svg=true)](https://ci.appveyor.com/project/chenjiandongx/pyhtime/branch/master) [![codecov](https://codecov.io/gh/chenjiandongx/pyhtime/branch/master/graph/badge.svg)](https://codecov.io/gh/chenjiandongx/pyhtime) [![PyPI version](https://badge.fury.io/py/pyhtime.svg)](https://badge.fury.io/py/pyhtime) ![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

htime 是一个用来将 datetime 时间转化成更加人性化的 `时间描述字符串`的库。灵感来自 [timeago.js](https://github.com/hustcc/timeago.js)。

#### 中文
* 刚刚
* 5 秒前
* 12 分钟前
* 3 小时后
* 3 个月前
* 2 年后

#### 英文
* just now
* 5 seconds ago
* 12 minutes ago
* 3 hours later
* 3 months ago
* 2 years later


### 安装
``` bash
$ pip install pyhtime
```


### 使用

#### API
pyhtime(when, base=None, local="zh")
* when: 想要转换的时间，可以为
    * 字符串格式："2018-4-1"
    * 英文时间："April 1, 2018"
    * 时间元组：(2018, 4, 1)
    * datetime.datetime 类型：datetime.datetime(2018, 4, 1)
* base: 基准时间，默认为`datetime.datetime.now()`，类型同`when`
* local: 显示语言，默认为中文'zh',可选英文为'en'


#### 示例
``` bash
>>> from pyhtime import htime
>>> import datetime
>>> datetime.datetime.now()
'datetime.datetime(2018, 4, 2, 17, 2, 17, 193371)'

# 字符串
>>> pyhtime("2018-4-1")
'1 天前'

# 时间元组
>>> pyhtime((2018, 4, 1))
'1 天前'

# datetime.datetime 类型
>>> pyhtime(datetime.datetime(2018, 4, 1))
'1 天前'

# 指定语言为英文
>>> pyhtime((2018, 4, 1), local="en")
'1 day ago'

# 英文时间格式
>>> pyhtime("April 1, 2018", local="en")
'1 day ago'

>>> pyhtime(datetime.datetime.now(), local="en")
'just now'

# 指定基准时间
>>> pyhtime("2018-8-8", "2008-8-8")
'10 年后'
```

### 测试
``` bash
$ make
```

### LICENSE
MIT [@chenjiandongx](https://github.com/chenjiandongx)

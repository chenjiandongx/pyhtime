# pytimeago

pytimeago 是一个用来将 datetime 时间转化成更加人性化的 `时间描述字符串`。灵感来自 [timeago.js](https://github.com/hustcc/timeago.js)。

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
$ pip install pytimeago
```


### 使用

#### API
timeago(when, base=None, local="zh")
* when: 想要转换的时间，可以为
    * 字符串格式："2018-4-1"
    * 英文时间："April 1, 2018"
    * 时间元组：(2018, 4, 1)
    * datetime.datetime 类型：datetime.datetime(2018, 4, 1)
* base: 基准时间，默认为`datetime.datetime.now()`，类型同`when`
* local: 显示语言，默认为中文'zh',可选英文为'en'


#### 示例
``` bash
>>> from pytimeago import timeago
>>> import datetime
>>> datetime.datetime.now()
'datetime.datetime(2018, 4, 2, 17, 2, 17, 193371)'

# 字符串
>>> timeago("2018-4-1")
'1 天前'

# 时间元组
>>> timeago((2018, 4, 1))
'1 天前'

# datetime.datetime 类型
>>> timeago(datetime.datetime(2018, 4, 1))
'1 天前'

# 指定语言为英文
>>> timeago((2018, 4, 1), local="en")
'1 day ago'

# 英文时间格式
>>> timeago("April 1, 2018", local="en")
'1 day ago'

>>> timeago(datetime.datetime.now(), local="en")
'just now'

# 指定基准时间
>>> timeago("2018-8-8", "2008-8-8")
'10 年后'
```

### 测试
``` bash
$ make
```

### LICENSE
MIT [@chenjiandongx](https://github.com/chenjiandongx)

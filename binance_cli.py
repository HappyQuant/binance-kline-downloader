#!/usr/bin/env python
# encoding: utf-8

import requests
import time
from enum import Enum


class KLineSymbol(Enum):
    BtcUsdt = "BTCUSDT"
    EthUsdt = "ETHUSDT"


class KLineInterval(Enum):
    OneMinute = "1m"
    ThreeMinute = "3m"
    FiveMinute = "5m"
    FifteenMinute = "15m"
    ThirtyMinute = "30m"
    OneHour = "1h"
    TwoHour = "2h"
    FourHour = "4h"
    SixHour = "6h"
    EightHour = "8h"
    TwelveHour = "12h"
    OneDay = "1d"


def fetch_klines(symbol: KLineSymbol, interval: KLineInterval,
                 endtime_ms: int = int(time.time()) * 1000,
                 limit: int = 1000, proxies: dict = None) -> str:
    assert limit <= 1000
    url = 'https://www.binance.com/api/v3/uiKlines?endTime={}&limit={}&symbol={}&interval={}' \
        .format(endtime_ms, limit, symbol.value, interval.value)
    resp = requests.get(url=url, proxies=proxies)
    return resp.text

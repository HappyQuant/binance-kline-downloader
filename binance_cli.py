#!/usr/bin/env python
# encoding: utf-8

import requests
import time
from enum import Enum
from utils import dt


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


def fetch_k_line_data(symbol: str, interval: KLineInterval, limit: int = 1000,
                      end_time: int = int(time.time()), proxies: dict = None) -> str:
    assert limit <= 1000
    url = 'https://www.binance.com/api/v3/uiKlines?endTime={}&limit={}&symbol={}&interval={}' \
        .format(dt.utc_last_ms_in_day(end_time), limit, symbol, interval.value)
    resp = requests.get(url=url, proxies=proxies)
    return resp.text

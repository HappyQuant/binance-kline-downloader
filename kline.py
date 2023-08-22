#!/usr/bin/env python
# encoding: utf-8
import json

from binance_cli import KLineSymbol, KLineInterval
from binance_cli import fetch_klines
from datetime import datetime, timezone
from utils import dt


def fetch_all_klines_for_day(symbol: KLineSymbol, interval: KLineInterval,
                             date: int, proxies: dict = None) -> list:
    year = date // 10000
    month = (date % 10000) // 100
    day = (date % 10000) % 100
    t = datetime(year=year, month=month, day=day, tzinfo=timezone.utc)
    ts = int(t.timestamp())
    first_ms = dt.utc_first_ms_in_day(ts)
    last_ms = dt.utc_last_ms_in_day(ts)

    day_klines = list()
    while last_ms > first_ms:
        s = fetch_klines(symbol=symbol, interval=interval,
                         endtime_ms=last_ms, proxies=proxies)
        ks = json.loads(s)[::-1]
        if len(ks) == 0 or ks[0][0] < first_ms:
            return day_klines[::-1]

        for k in ks:
            if k[0] >= first_ms:
                day_klines.append(k)
                last_ms = k[0] - 1
            else:
                break

    return day_klines[::-1]

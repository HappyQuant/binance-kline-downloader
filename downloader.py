#!/usr/bin/env python
# encoding: utf-8
import json
import time

from binance_cli import KLineSymbol, KLineInterval
from kline import fetch_all_klines_for_day
from utils import dt
import os

data_dir = "data"
kline_symbol = KLineSymbol.EthUsdt
kline_interval = KLineInterval.OneMinute

data_path = "{}/{}/{}".format(data_dir, kline_symbol.value, kline_interval.value)
if not os.path.exists(data_path):
    os.makedirs(data_path)

ts_now = int(time.time())
ts_start = ts_now - dt.SECONDS_PER_DAY

while True:
    ts_date = dt.utc_ts_to_date(ts_start)
    data_file = "{}/{}".format(data_path, ts_date)
    if os.path.exists(data_file):
        ts_start -= dt.SECONDS_PER_DAY
        continue

    klines = fetch_all_klines_for_day(symbol=kline_symbol, interval=kline_interval, date=ts_date,
                                      proxies={"socks5": "socks5://127.0.0.1:1080"})
    if len(klines) == 0:
        break

    s = json.dumps(klines, indent=4)
    w = open(data_file, "w")
    w.write(s)
    w.close()
    print("download %s" % data_file)

    ts_start -= dt.SECONDS_PER_DAY

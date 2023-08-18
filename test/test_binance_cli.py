#!/usr/bin/env python
# encoding: utf-8
import json
import time
import unittest
from binance_cli import fetch_klines
from binance_cli import KLineInterval, KLineSymbol


class TestBinanceCli(unittest.TestCase):
    def test_fetch_klines(self):
        r = fetch_klines(symbol=KLineSymbol.BtcUsdt, interval=KLineInterval.OneMinute,
                         endtime_ms=int(time.time()) * 1000, limit=1000,
                         proxies={"socks5": "socks5://127.0.0.1:1080"})
        o = json.loads(r)
        self.assertEqual(len(o), len(o))

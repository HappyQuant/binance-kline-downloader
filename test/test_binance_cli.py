#!/usr/bin/env python
# encoding: utf-8
import json
import time
import unittest
from binance_cli import fetch_k_line_data
from binance_cli import KLineInterval


class TestBinanceCli(unittest.TestCase):
    def test_fetch_k_line_data(self):
        r = fetch_k_line_data(symbol="BTCUSDT", interval=KLineInterval.OneMinute,
                              limit=1000, end_time=int(time.time()),
                              proxies={"socks5": "socks5://127.0.0.1:1080"})
        o = json.loads(r)
        self.assertEqual(len(o), len(o))

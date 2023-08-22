#!/usr/bin/env python
# encoding: utf-8
import unittest

from binance_cli import KLineSymbol, KLineInterval
from kline import fetch_all_klines_for_day


class TestKline(unittest.TestCase):
    def test_fetch_all_klines_for_day(self):
        ks = fetch_all_klines_for_day(symbol=KLineSymbol.BtcUsdt, interval=KLineInterval.OneMinute,
                                      date=20220820, proxies={"socks5": "socks5://127.0.0.1:1080"})
        self.assertEqual(len(ks), 1440)

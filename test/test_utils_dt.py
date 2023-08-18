#!/usr/bin/env python
# encoding: utf-8

import unittest
from utils import dt


class TestUtilsDt(unittest.TestCase):
    def test_utc_first_ts_in_day(self):
        self.assertEqual(dt.utc_first_ts_in_day(1692341320), 1692316800)

    def test_utc_last_ts_in_day(self):
        self.assertEqual(dt.utc_last_ts_in_day(1692341320), 1692403199)

    def test_utc_first_ms_in_day(self):
        self.assertEqual(dt.utc_first_ms_in_day(1692341320), 1692316800000)

    def test_utc_last_ms_in_day(self):
        self.assertEqual(dt.utc_last_ms_in_day(1692341320), 1692403199999)

    def test_utc_ts_to_date(self):
        self.assertEqual(dt.utc_ts_to_date(1692341320), 20230818)

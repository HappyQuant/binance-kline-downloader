#!/usr/bin/env python
# encoding: utf-8


from datetime import datetime

SECONDS_PER_DAY = 86400


def utc_first_ts_in_day(ts: int) -> int:
    return ts // SECONDS_PER_DAY * SECONDS_PER_DAY


def utc_last_ts_in_day(ts: int) -> int:
    return (ts // SECONDS_PER_DAY + 1) * SECONDS_PER_DAY - 1


def utc_first_ms_in_day(ts: int) -> int:
    return utc_first_ts_in_day(ts) * 1000


def utc_last_ms_in_day(ts: int) -> int:
    return utc_last_ts_in_day(ts) * 1000 + 999


def utc_ts_to_date(ts: int) -> int:
    d = datetime.utcfromtimestamp(ts)
    return d.year * 10000 + d.month * 100 + d.day

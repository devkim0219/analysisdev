import pandas as pd

# TimeStamp 의 배열 만들기 - 월 간격, 월의 시작일 기준
ts_ms = pd.date_range(start='2019-01-01',
                      end=None,
                      periods=6,
                      freq='MS',
                      tz='Asia/Seoul')

print(ts_ms)

# 월 간격, 월의 마지막 날 기준
ts_me = pd.date_range(start='2019-01-01',
                      periods=6,
                      freq='M',
                      tz='Asia/Seoul')

print(ts_me)

# 분기(3개월) 간격, 월의 마지막 날 기준
ts_3m = pd.date_range(start='2019-01-01',
                      periods=6,
                      freq='3M',
                      tz='Asia/Seoul')

print(ts_3m)
# _*_ coding: utf-8 _*_
__file__ = '行为金融 test1.py'
__author__ = 'zhiyi'
__date__ = '2017/3/30 18:14'
__vers__ = '1.0'

import pandas as pd

date_index = pd.date_range('2013-01-31', '2015-12-31', freq='M', normalize=True)
# print(date_index)
df = pd.DataFrame(index=date_index)
print(df)
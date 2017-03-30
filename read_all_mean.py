# _*_ coding: utf-8 _*_
__file__ = '行为金融 read_all_mean.py'
__author__ = 'zhiyi'
__date__ = '2017/3/30 20:33'
__vers__ = '1.0'
import os
import pandas as pd
import numpy as np


output_path = 'F:\\360data\\重要数据\\桌面\\暂时杂物\\小公司效应\\output'
group_yield_file = ['a_group_yield_mean.csv', 'b_group_yield_mean.csv', 'c_group_yield_mean.csv',
                    'd_group_yield_mean.csv', 'e_group_yield_mean.csv']
df = pd.DataFrame()
for file in group_yield_file:
    yield_mean = pd.read_csv(os.path.join(output_path, file), encoding='utf8', index_col='date')['mean']
    df['{}'.format(file[:7])] = yield_mean
# df = df.interpolate(method='linear')
# df.to_csv(os.path.join(output_path, 'all_yield_mean.csv'), encoding='utf8', index=True)
print(df)
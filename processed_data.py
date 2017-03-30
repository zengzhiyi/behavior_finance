# _*_ coding: utf-8 _*_
__file__ = '行为金融 processed_data.py'
__author__ = 'zhiyi'
__date__ = '2017/3/30 17:54'
__vers__ = '1.0'
import os
import pandas as pd
import numpy as np

p2_path = 'F:\\360data\\重要数据\\桌面\\暂时杂物\\小公司效应\\processed_data\\p2'
output_path = 'F:\\360data\\重要数据\\桌面\\暂时杂物\\小公司效应\\output'

groups_path = ['a_group', 'b_group', 'c_group', 'd_group', 'e_group']
for file_path in groups_path:
    path = p2_path + '\\' + file_path
    # date_index = pd.date_range('2013-01-31', '2015-12-31', freq='M', normalize=True)
    group_yield_mean = pd.DataFrame()
    for root, dirs, files in os.walk(path):
        for file in files:
            raw_df = pd.read_csv(os.path.join(path, file), encoding='utf8', index_col='date')
            group_yield_mean['{}'.format(file[:6])] = raw_df['yield']
            # group_yield_mean = pd.concat([group_yield_mean, raw_df['yield']], axis=1)
    print(group_yield_mean)
    group_yield_mean['mean'] = group_yield_mean.mean(axis=1)
    group_yield_mean = group_yield_mean.interpolate(method='linear')
    group_yield_mean.to_csv(os.path.join(output_path, file_path + '_yield_mean.csv'), encoding='utf8')
    print(group_yield_mean)
    # print(file_path, 'done')

# _*_ coding: utf-8 _*_
__file__ = '行为金融 pre_process.py'
__author__ = 'zhiyi'
__date__ = '2017/3/30 16:26'
__vers__ = '1.0'
# _*_ coding: utf-8 _*_
import tushare as ts
import os
import pandas as pd
import time
import numpy as np

raw_data_file_path = 'F:\\360data\\重要数据\\桌面\\暂时杂物\\小公司效应\\raw_data'
groups_file_path = ['a_group', 'b_group', 'c_group',
                    'd_group', 'e_group']
code_files = ['a_group', 'b_group', 'c_group',
              'd_group', 'e_group']

def read_and_count_len_df():
    for file_path in groups_file_path:
        path = raw_data_file_path + '\\' + file_path
        for root, dirs, files in os.walk(path):
            for file in files:
                raw_df = pd.read_csv(os.path.join(path, file), encoding='utf8', index_col='code')
                yield_df = np.log(raw_df['close']).diff(1)
                raw_df['yield'] = yield_df
                # raw_df.to_csv(os.path.join(path, file), encoding='utf8', index=None)
                print(yield_df)



if __name__ == '__main__':
    read_and_count_len_df()
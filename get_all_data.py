# _*_ coding: utf-8 _*_
__file__ = '行为金融 get_all_data.py'
__author__ = 'zhiyi'
__date__ = '2017/3/30 14:10'
__vers__ = '1.0'
import tushare as ts
import os
import pandas as pd
import time
import numpy as np


raw_data_file_path = 'F:\\360data\\重要数据\\桌面\\暂时杂物\\小公司效应\\raw_data'
processed_data_path = 'F:\\360data\\重要数据\\桌面\\暂时杂物\\小公司效应\\processed_data'
groups_file_path = ['a_group', 'b_group', 'c_group',
                    'd_group', 'e_group']
code_files = ['a_group', 'b_group', 'c_group',
              'd_group', 'e_group']

def read_and_get_data():
    wrong = {}
    for file in code_files:
        code_df = pd.read_csv(os.path.join(processed_data_path, file + '.csv'), encoding='gbk')
        code_list = code_df['代码'].astype(str)
        n = 0
        for code in code_list:
            time.sleep(0.1)
            if len(code) < 6:
                code = '0' * (6 - len(code)) + code
            try:
                raw_df = ts.get_k_data(code, ktype='M', autype='hfq', start='2012-12-01', end='2016-01-01')
                raw_df['code'] = raw_df['code'].astype(str)
                if len(raw_df) < 36:
                    continue
                yield_df = np.log(raw_df['close']).diff(1)
                raw_df['yield'] = yield_df
                raw_df.dropna(how='any', inplace=True)
                raw_df['date'] = pd.to_datetime(raw_df['date'], format='%Y-%m-%d')
                raw_df.to_csv(os.path.join(raw_data_file_path + '\\' + file, code + '.csv'), encoding='utf8', index=None)
                print(raw_df)
                print(code, '  done')
            except IndexError as idr:
                n += 1
                pass
        time.sleep(0.5)
        wrong['{}_group'.format(file[:2])] = n
    print(wrong)

if __name__ == '__main__':
    read_and_get_data()
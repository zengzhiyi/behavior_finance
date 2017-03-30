# _*_ coding: utf-8 _*_
__file__ = '行为金融 plot_bar.py'
__author__ = 'zhiyi'
__date__ = '2017/3/30 18:28'
__vers__ = '1.0'
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['font.size'] = 10
plt.rcParams['lines.linewidth'] = 2

# 1、read 5 csv: group_yield_mean['mean]
# 2、plot 36 months bar
output_path = 'F:\\360data\\重要数据\\桌面\\暂时杂物\\小公司效应\\output'
group_yield_file = ['a_group_yield_mean.csv', 'b_group_yield_mean.csv', 'c_group_yield_mean.csv',
                    'd_group_yield_mean.csv', 'e_group_yield_mean.csv']
fig = plt.figure(figsize=(18, 6))
width = 0.15
ax = fig.add_subplot(111)
x = np.arange(36)
# for file in group_yield_file:
ax.set_xticks([i for i in range(37)])

ax.set_xticklabels(['2013-01', '2013-02', '2013-03', '2013-04', '2013-05', '2013-06', '2013-07', '2013-08', '2013-09', '2013-10', '2013-11', '2013-12',
                    '2014-01', '2014-02', '2014-03', '2014-04', '2014-05', '2014-06', '2014-07', '2014-08', '2014-09', '2014-10', '2014-11', '2014-12',
                    '2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06', '2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12'],
                   rotation=30)

# y = 0 画一条大红线
# l = plt.axhline(linewidth=8, color='#d62728')

# x = 1 画一条线
# v = plt.axvline(x=1)

# x = 1, ymin=0.75
# vl = plt.axvline(x=1, ymin=0.75, linewidth=8, color='#1f77b4')

# h1 = plt.axhspan(ymin=-0.2, ymax=0.2, xmin=0, xmax=0.327, facecolor='0.6', alpha=0.5)
# h2 = plt.axhspan(ymin=-0.2, ymax=0.2, xmin=0.328, xmax=0.67, facecolor='0.3', alpha=0.5)
# h3 = plt.axhspan(ymin=-0.2, ymax=0.2, xmin=0.67, xmax=1., facecolor='0.6', alpha=0.5)

wid = 3
v1 = plt.axvspan(xmin=0 + wid, xmax=1 + wid, facecolor='g', alpha=0.5)
v2 = plt.axvspan(xmin=12 + wid, xmax=13 + wid, facecolor='g', alpha=0.5)
v3 = plt.axvspan(xmin=24 + wid, xmax=25 + wid, facecolor='g', alpha=0.5)

a_group_yield_mean = pd.read_csv(os.path.join(output_path, group_yield_file[0]), encoding='utf8', index_col='date')['mean']
ax.bar(x + width * 0, height=a_group_yield_mean, width=width, color='red')

b_group_yield_mean = pd.read_csv(os.path.join(output_path, group_yield_file[1]), encoding='utf8', index_col='date')['mean']
ax.bar(x + width * 1, height=b_group_yield_mean, width=width, color='blue')

c_group_yield_mean = pd.read_csv(os.path.join(output_path, group_yield_file[2]), encoding='utf8', index_col='date')['mean']
ax.bar(x + width * 2, height=c_group_yield_mean, width=width, color='yellow')

d_group_yield_mean = pd.read_csv(os.path.join(output_path, group_yield_file[3]), encoding='utf8', index_col='date')['mean']
ax.bar(x + width * 3, height=d_group_yield_mean, width=width, color='green')

e_group_yield_mean = pd.read_csv(os.path.join(output_path, group_yield_file[4]), encoding='utf8', index_col='date')['mean']
ax.bar(x + width * 4, height=e_group_yield_mean, width=width, color='black')

plt.tight_layout()
plt.show()

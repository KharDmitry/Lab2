import urllib.request
import pandas as pd
from datetime import datetime
import numpy as np
headers = ['Year', 'Week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI', 'empty']
max_df = {}
min_df = {}
data_max = pd.DataFrame()
data_min = pd.DataFrame()
area = ['a', 'b', 'c','a', 'b', 'c','a', 'b', 'c', 'a', 'b', 'c','a', 'b', 'c','a', 'b', 'c', 'a', 'b', 'c','a', 'b', 'c','a', 'b', 'c']
for i in range(1, 28):
    url='https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?country=UKR&provinceID={}&year1=2014&year2=2021&type=Mean'.format(i)
    wp = urllib.request.urlopen(url)
    text = wp.read()
    now = datetime.now()
    out = open('obl{}'.format(i) + '.csv', 'wb') # now.strftime("%d%m%Y%H%M%S") +
    out.write(text)
    out.close()
for i in range(1, 28):
    df = pd.read_csv('D:\Dima\Spec_proga\lab1\obl{}.csv'.format(i), header = 1, names = headers)
    df = df.drop(df.loc[df['VHI'] == -1].index)
    df['area'] = i
    #df["area"].replace({i: ((i + 3)%27) + 1}, inplace=True)
    for j in range(2014, 2022):
        j = str(j)
        a = df[df['Year'].isin([j])]
        max_df[j] = a['VHI'].max()
    for k in range(2014, 2022):
        k = str(k)
        a = df[df['Year'].isin([k])]
        min_df[k] = a['VHI'].min()
    data_max = data_max.append(max_df, ignore_index=True)
    data_min = data_min.append(min_df, ignore_index=True)
data_max.index = np.arange(1, len(data_max) + 1)
data_min.index = np.arange(1, len(data_min) + 1)
print(data_max)
print(data_min)




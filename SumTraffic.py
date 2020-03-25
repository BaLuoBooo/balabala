# -*- coding:utf-8 -*-
# @Time: 2020/3/25 16:49
# @Author: BaLuoBooooo
# @Email: 1xxxxxxx@qq.com
# @File: SumTraffic.py
# @Function:统计整体用户流量使用情况
import os
import pandas as pd
import numpy as np
from Visulization.DrawGraph import Graph
def count():
    x_data =[]
    G = Graph()
    files = os.walk('./res')
    traffic = []
    for root, dirs, file in files:
        for sub_file in file:
            sum = 0.0
            path = './res/{}'.format(sub_file)
            df = pd.read_excel(path,usecols=[5])
            xaxi_name = sub_file.replace('.xlsx','')
            test = np.array(df)
            for row in range(len(test)):
                print(test[row, 0])
                clear_data = test[row, 0].replace(',','')
                sum = sum + float(clear_data/len(test))
            #print(sum)
            traffic.append(sum)
            print(traffic)
            x_data.append(xaxi_name)
            G.draw_bar(x_data,traffic,'total')


if __name__ == '__main__':
    count()
    G = Graph()

# -*- coding:utf-8 -*-
# @Time: 2020/3/25 18:33
# @Author: BaLuoBooooo
# @Email: 1xxxxxxx@qq.com
# @File: TraDestri.py
# @Function:
import os
import pandas as pd
import numpy as np
from Visulization.DrawGraph import Graph
from TrafficDesribute.DataClassify import ClassifyData
class Destribute:
    def traffic_destribute(self):
        #print(x_data)
        #print(x_data)
        files = os.walk('./res')
        G = Graph()
        CD = ClassifyData()
        #print(files)
        for root, dirs, file in files:
            for sub_file in file:
                x_data = []
                #print(traffic)
                path = './res/{}'.format(sub_file)
                df = pd.read_excel(path,usecols=[5])
                xaxi_name = sub_file.replace('.xlsx','')
                test = np.array(df)
                row_data = []
                #从NP中循环读取，放入list中
                for row in range(len(test)):  #循环读取np中的数据
                    print(test[row, 0])
                    line_data = float(str(test[row, 0]).replace(',',''))
                    row_data.append(line_data)
                #np_line =np.array(row_data)
                #选择list最大值，确定链表区间

                max_number = max(row_data)
                #print(max_number)
                traffic = list([0 for index in range(int(1000/50)+1)])
                #print(traffic)
                zero_use = 0
                #确定y轴的数值
                for sub_data in row_data:
                    index = CD.classify_data(sub_data)
                    #print(index)
                    if index >= 0:
                        traffic[index] = traffic[index] + 1
                    else:
                        zero_use = zero_use + 1
                #print(traffic)
                #确定x轴区间的大小
                for i in range(int(1000/50)):
                    sub_x = []
                    sub_x.append(i * 50)
                    x_data.append(sub_x)
                x_data.append('>1G')
                print(x_data)
                title = xaxi_name +' max:'+str(max_number)+' zerouse:'+str(zero_use)
                G.draw_bar(x_data,traffic,xaxi_name,title)
                print(len(x_data))
                print(len(traffic))
                print(zero_use)




if __name__ == '__main__':
    D = Destribute()
    D.traffic_destribute()


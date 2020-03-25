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
class Destribute:
    def traffic_destribute(self):
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
                    lear_data = test[row, 0].replace(',','')
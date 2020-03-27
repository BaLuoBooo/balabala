# -*- coding:utf-8 -*-
# @Time: 2020/3/26 11:08
# @Author: BaLuoBooooo
# @Email: 1xxxxxxx@qq.com
# @File: CutDataWiDate.py
# @Function:
import numpy as np
import pandas as pd
from Visulization.DrawGraph import Graph
from TrafficDesribute.DataClassify import ClassifyData
class CutData:
    def date_format(self,data):
        date = str(data)
        date_list = date.split('-')
        mouth = date_list[1]
        year = date_list[0].split("'")[0]
        return mouth,year

    def cut_renewal_data(self):
        date_iccid = {}
        #读取文件中的所有ICCID与对应的年月,返回各个iccid对应的date
        origin_data_path = '../TotalData/orderpay.xls'
        df = pd.read_excel(origin_data_path)
        df = pd.DataFrame(df)
        for i in range(201905,201913):
            date_iccid[str(i)] = []
        for i in range(202001,202004):
            date_iccid[str(i)] = []
        for data in df.values:
            #print(flag)
            mouth, year = self.date_format(data[1])
            path = year + mouth #201905
            iccid = data[0] #iccid
            date_iccid[path].append(iccid)
        #print(date_iccid)
        return date_iccid


    def query_traffic_mouth(self,path,iccid_list):
        #通过iccid找到对应文件中的流量,返回对应的流量数目
        path = '../res/'+path+'.xlsx'
        df = pd.read_excel(path, usecols=[0,5])
        da = df.to_dict(orient='records')
        traffic_list = []
        for sub_da in da:
            for sub_icc_list in iccid_list:
                if sub_da['ICCID'] == sub_icc_list:
                    traffic = sub_da['流量 (MB)']
                    traffic_list.append(traffic)
        #print(path)
        #print(iccid_list)
        return traffic_list

    def draw_graph(self,data_list,name):
        #
        re_renewal_number = {}
        x_data = []
        G = Graph()
        CD = ClassifyData()
        zero_use = 0
        traffic = list([0 for index in range(int(1000/50)+1)]) #数量统计
        traffic_list = []  #没项消耗的人数
        re_renewal_number[name] = []
        for sub_date in data_list: #获取图表中Y轴的数据
            line_data = float(str(sub_date).replace(',',''))
            traffic_list.append(line_data)
            index = CD.classify_data(float(line_data))
            if index >= 0:
                traffic[index] = traffic[index] + 1
            else:
                zero_use = zero_use + 1
        max_number = max(traffic_list)
        print('max_number='+ str(max_number))
        for i in range(int(1000 / 50)): #获取图标中的
            sub_x = []
            sub_x.append(i * 50)
            x_data.append(sub_x)
        x_data.append('>1G')
        print(x_data)
        #title = name + ' max:' + str(max_number) + ' zerouse:' + str(zero_use)
        #print(x_data)
        #print(traffic)
        #G.draw_dymatic_bar(x_data,traffic,name,title)
        re_renewal_number[name] = traffic
        print(re_renewal_number)
        return re_renewal_number,x_data

if __name__ == '__main__':
    CD = CutData()
    G = Graph()
    date_icc = CD.cut_renewal_data() #某月的续费iccid
    total_traffic_list = []
    x_data = []
    #print(date_icc)
    for sub_icc_date in date_icc.items():
        date = sub_icc_date[0]
        iccid_list = sub_icc_date[1]
        #print(iccid_list)
        traffic = CD.query_traffic_mouth(date,iccid_list) #单月续费用户的流量消耗
        #print(traffic)
        month_traffic_dict,x_data = CD.draw_graph(traffic,date)
        #total_traffic_list.append(month_traffic_dict)

    #G.draw_multi_bar(total_traffic_list,x_data,'total')





# -*- coding:utf-8 -*-
# @Time: 2020/3/27 13:09
# @Author: BaLuoBooooo
# @Email: 1xxxxxxx@qq.com
# @File: UnderFifty.py
# @Function:
from TrafficDesribute.DataClassify import ClassifyData
from TrafficOrder.CutDataWiDate import CutData
from HistoryNowTrafficOrder.HisNowData import HistoryNowData
from Visulization.DrawGraph import Graph
class FiftyUser:
    #获取x轴的刻度
    def gain_x_date(self,min_size,traffic_list,traffic_threshold):
        x_data = []
        #max_traffic = max(traffic_list)
        part_number = int(traffic_threshold/min_size)
        for i in range(part_number+1):
            x_data.append(str(i*min_size))
        return x_data

    #将流量划分为各区域的人数数量
    def traffic_list2_numbe_listr(self,min_size,traffic_list,traffic_threshold):
        zero_use = 0
        number_list = list([0 for index in range(int(traffic_threshold / min_size) + 1)]) #各层的流量转换为人数
        for sub_date in traffic_list:  # 获取图表中Y轴的数据
            print(len(number_list))
            index = self.traffic2_number(min_size,sub_date)
            print('index=',index)
            number_list[index] = number_list[index] + 1
        return number_list

    # 确定所需要绘图的流量区间
    def traffic_area(self,traffic_threshold,traffic_list):
        threshold_traffic_list = []
        for sub_data in traffic_list:
            if sub_data < traffic_threshold:
                threshold_traffic_list.append(sub_data)
        return threshold_traffic_list

    # 清洗流量数据
    def traffic_list_clear(self,traffic_list):
        clear_traffic_list = []
        for sub_data in traffic_list:
            clear_data = float(str(sub_data).replace(',', ''))
            clear_traffic_list.append(clear_data)
        return clear_traffic_list

    # 按照最小划分
    def traffic2_number(self,min_size,traffic_data):
        index = 0
        if traffic_data!= 0:
            index = traffic_data/min_size
            #print(int(index))
        else:
            return 0
        return int(index)+1


if __name__ == '__main__':
    G = Graph()
    fu = FiftyUser()
    HD = HistoryNowData()
    x_data = []
    Whole_number_list = []
    Whole_date_list = []
    Whole_zero_list = []
    #获得每个月份的ICCID
    total_renewal_user = HD.gain_month_renewal_user()
    for sub_icc_date in total_renewal_user.items():
        pre_cur_suf = []
        date = sub_icc_date[0]
        iccid_list = sub_icc_date[1]
        #获得当前月份的流量,返回为流量的列表
        current_traffic = HD.query_current_month(date, iccid_list)
        #清洗流量列表，筛选流量区间，清洗流量数据
        clear_traffic = fu.traffic_list_clear(current_traffic)
        traffic_area = fu.traffic_area(50,clear_traffic)
        #print(traffic_area)
        #获取x轴的坐标粒度
        x_data = fu.gain_x_date(10,clear_traffic,50)
        #print(x_data)
        number = fu.traffic_list2_numbe_listr(10,traffic_area,50)
        Whole_number_list.append(number)
        Whole_date_list.append(date)
        #Whole_zero_list.append(zero)
        #G.draw_bar(x_data,number,date,date)
    G.draw_multi_graph(Whole_number_list,Whole_date_list,Whole_zero_list,x_data)




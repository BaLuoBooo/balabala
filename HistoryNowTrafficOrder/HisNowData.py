# -*- coding:utf-8 -*-
# @Time: 2020/3/26 17:03
# @Author: BaLuoBooooo
# @Email: 1xxxxxxx@qq.com
# @File: HisNowData.py
# @Function:展现当前月份续费用户，前一个月与后一个月的流量使用情况
import pandas as pd
from TrafficDesribute.DataClassify import ClassifyData
from Visulization.DrawGraph import Graph
from TrafficOrder.CutDataWiDate import CutData
class HistoryNowData:
    def gain_month_renewal_user(self):
        #获取每月的续费用户的iccid
        CD = CutData()
        date_iccid = {}
        origin_data_path = '../TotalData/orderpay.xls'
        df = pd.read_excel(origin_data_path)
        df = pd.DataFrame(df)
        for i in range(201905, 201913):
          date_iccid[str(i)] = []
        for data in df.values:
            mouth, year = CD.date_format(data[1])
            path = year + mouth  # 201905
            if int(path)<201913:
                iccid = data[0]  # iccid
                date_iccid[path].append(iccid)
        return date_iccid

    def query_current_month(self,date,iccid_list):
        curr_date_traffic_dict = {}
        traffic_list = []
        path = '../res/' + str(date) + '.xlsx'
        curr_date_traffic_dict[str(date)] = []
        df = pd.read_excel(path, usecols=[0, 5])  # 读取iccid与流量消耗
        da = df.to_dict(orient='records')  # DataFrame转为dict
        for sub_da in da:
            for sub_icc_list in iccid_list:
                if sub_da['ICCID'] == sub_icc_list:
                    traffic = sub_da['流量 (MB)']
                    traffic_list.append(traffic)
        curr_date_traffic_dict[str(date)] = traffic_list
        return traffic_list

    def query_pre_month(self,date,iccid_list):
        #获取当月续费用户上个月的流量
        #输入为月份与续费iccid
        pre_date_traffic = {}
        traffic_list = []
        per_date = int(date) - 1
        path ='../res/'+str(per_date)+'.xlsx'
        pre_date_traffic[str(per_date)] = []
        df = pd.read_excel(path, usecols=[0, 5]) #读取iccid与流量消耗
        da = df.to_dict(orient='records') #DataFrame转为dict
        for sub_da in da:
            for sub_icc_list in iccid_list:
                if sub_da['ICCID'] == sub_icc_list:
                    traffic = sub_da['流量 (MB)']
                    traffic_list.append(traffic)
        pre_date_traffic[str(per_date)] = traffic_list
        return traffic_list

    def query_suffix_month(self,date,iccid_list):
        #获取当月续费用户下个月的流量
        suffix_date_traffic = {}
        traffic_list = []
        if date == 201912:
            return 0
        suffix_date = int(date) + 1
        path = '../res/' + str(suffix_date) + '.xlsx'
        suffix_date_traffic[str(suffix_date)] = []
        df = pd.read_excel(path, usecols=[0, 5])  # 读取iccid与流量消耗
        da = df.to_dict(orient='records')  # DataFrame转为dict
        for sub_da in da:
            for sub_icc_list in iccid_list:
                if sub_da['ICCID'] == sub_icc_list:
                    traffic = sub_da['流量 (MB)']
                    traffic_list.append(traffic)
        suffix_date_traffic[str(suffix_date)] = traffic_list
        return traffic_list


    def traffic2number(self,date,traffic_list):
        #将流量转换为分段人数
        zero_use = 0
        CD = ClassifyData()
        x_data = []
        date_number_list = {}
        number_list = list([0 for index in range(int(1000 / 50) + 1)])  # 数量统计
        clear_traffic_list = []  # 单月的流量的集合
        for sub_date in traffic_list: #获取图表中Y轴的数据
            line_data = float(str(sub_date).replace(',',''))
            clear_traffic_list.append(line_data)
            index = CD.classify_data(float(line_data))
            if index >= 0:
                number_list[index] = number_list[index] + 1
            else:
                zero_use = zero_use + 1
        max_number = max(clear_traffic_list)
        print('max_number='+ str(max_number))
        date_number_list[date] = []
        for i in range(int(1000 / 50)): #获取图标中的
            sub_x = []
            sub_x.append(i * 50)
            x_data.append(sub_x)
        x_data.append('>1G')
        #date_number_list[date] = number_list
        return number_list


if __name__ == '__main__':
    HD = HistoryNowData()
    G = Graph()
    #获取所有月份续费用户的iccid
    total_user = HD.gain_month_renewal_user()
    for sub_icc_date in total_user.items():
        pre_cur_suf = []
        date = sub_icc_date[0]
        iccid_list = sub_icc_date[1]
        pre_traffic = HD.query_pre_month(date,iccid_list)
        suffix_traffic = HD.query_suffix_month(date,iccid_list)
        current_traffic = HD.query_current_month(date,iccid_list)
        pre_number = HD.traffic2number(date,pre_traffic)
        suffix_number = HD.traffic2number(date,suffix_traffic)
        current_number = HD.traffic2number(date,current_traffic)
        pre_cur_suf.append(pre_number)
        pre_cur_suf.append(current_number)
        pre_cur_suf.append(suffix_number)
        G.draw_multi_graph(pre_cur_suf,date)




    #获取当前用户上个月的和下个月的流量
    #根据获取的流量确定Y轴坐标
    #输入x坐标与y坐标，整理图片
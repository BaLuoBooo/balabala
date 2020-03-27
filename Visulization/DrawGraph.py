# -*- coding:utf-8 -*-
# @Time: 2020/3/25 17:25
# @Author: BaLuoBooooo
# @Email: 1xxxxxxx@qq.com
# @File: DrawGraph.py
# @Function:画图
import pyecharts.charts as pyec
from pyecharts import options as opts
from pyecharts.charts import Bar
class Graph:
    def draw_bar(self,x_data,y_data,name,title):
        bar = pyec.Bar()
        bar.add_xaxis(x_data)
        bar.add_yaxis(series_name=title, yaxis_data=y_data)
        bar.render('../TotalUser/'+name+'.html')

    def draw_dymatic_bar(self, x_data, y_data, name, title):
        bar = pyec.Bar()
        bar.add_xaxis(x_data)
        bar.add_yaxis(series_name=title, yaxis_data=y_data)
        bar.render('./TotalData'+name+'.html')


    def draw_multi_bar(self):
        date = 0
        iccid_list = []
        x_data = [[0], [50], [100], [150], [200], [250], [300], [350], [400], [450], [500], [550], [600], [650], [700], [750], [800], [850], [900], [950], '>1G']
        v1 = [[8, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ,[64, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3]
        ,[63, 11, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        ,[197, 60, 26, 24, 17, 11, 14, 9, 6, 6, 6, 5, 6, 1, 5, 9, 4, 2, 2, 0, 116]
        ,[144, 52, 29, 17, 15, 11, 10, 6, 8, 3, 10, 8, 22, 17, 14, 10, 10, 7, 10, 0, 159]
        ,[1225, 507, 288, 192, 129, 90, 62, 71, 46, 28, 32, 29, 58, 43, 25, 21, 30, 11, 12, 0, 242]
        ,[416, 180, 146, 78, 49, 49, 46, 16, 23, 16, 13, 10, 15, 23, 18, 11, 15, 11, 4, 0, 215]
        ,[602, 244, 115, 83, 57, 37, 22, 35, 33, 27, 19, 13, 25, 22, 10, 15, 17, 13, 8, 0, 288]]
        bar = pyec.Bar()
        for i in range(201905,201913):
            bar.add_xaxis(x_data)
            bar.add_yaxis(series_name=str(i), yaxis_data=v1[i-201905])
            bar.overlap(bar)
        bar.render('../TotalData.html')

    def draw_multi_graph(self,Total_data, Total_date, Total_zero_use, x_data):
            bar = (Bar().add_xaxis(xaxis_data=x_data))
            for i in range(len(Total_data)):
                bar.add_yaxis(series_name=Total_date[i],yaxis_data=Total_data[i],is_selected=False,label_opts=opts.LabelOpts(is_show=False))
            bar.set_global_opts(datazoom_opts = [opts.DataZoomOpts(type_="inside")])
            bar.render('../TotalUser/51.html')









if __name__ == '__main__':
    G = Graph()
    G.draw_multi_bar()
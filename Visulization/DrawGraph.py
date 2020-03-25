# -*- coding:utf-8 -*-
# @Time: 2020/3/25 17:25
# @Author: BaLuoBooooo
# @Email: 1xxxxxxx@qq.com
# @File: DrawGraph.py
# @Function:画图
import pyecharts.charts as pyec
class Graph:
    def draw_bar(self,x_data,y_data,name):
        bar = pyec.Bar()
        bar.add_xaxis(x_data)
        bar.add_yaxis(series_name='precipitation', yaxis_data=y_data)
        bar.render(name+'.html')
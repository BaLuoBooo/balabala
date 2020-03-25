# -*- coding:utf-8 -*-
# @Time: 2020/3/25 18:38
# @Author: BaLuoBooooo
# @Email: 1xxxxxxx@qq.com
# @File: DataClassify.py
# @Function:
class ClassifyData:
    def classify_data(self,traffic_data):
        index = traffic_data/20
        print(int(index))


if __name__ == '__main__':
    CD = ClassifyData()
    CD.classify_data(21)
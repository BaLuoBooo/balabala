# -*- coding:utf-8 -*-
# @Time: 2020/3/25 18:38
# @Author: BaLuoBooooo
# @Email: 1xxxxxxx@qq.com
# @File: DataClassify.py
# @Function:
class ClassifyData:
    def classify_data(self,traffic_data):
        if traffic_data!= 0:
            index = traffic_data/50
            #print(int(index))
            if index < 19:
                return int(index)
            else:
                return 20
        else:
            return -1

if __name__ == '__main__':
    CD = ClassifyData()
    CD.classify_data(19.111)
# -*- coding:utf-8 -*-
# @Time: 2020/3/27 16:22
# @Author: BaLuoBooooo
# @Email: 1xxxxxxx@qq.com
# @File: CustomerUtil.py
# @Function：将所有用户进行分类
from CustomerClassfied.CarModel import model
import pandas as pd
class ClassifyCustomer:
    #根据车型区别iccid
    def customer_classfy(self,start_index,end_index):
        iccid_model = {}
        car_model = model.model_list
        path = './customer_classify.csv'
        data_set = pd.read_csv(path)
        for i in range(start_index,end_index):
            iccid_model[car_model[i]]= []
            for index, row in data_set.iterrows():
                if car_model[i] == row[1]:
                    iccid_model[car_model[i]].append(row[0])
            print(iccid_model)
        return iccid_model





if __name__ == '__main__':
    cc = ClassifyCustomer()
    cc.customer_classfy(2,5)
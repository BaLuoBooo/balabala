# -*- coding:utf-8 -*-
# @Time: 2020/3/27 17:29
# @Author: BaLuoBooooo
# @Email: 1xxxxxxx@qq.com
# @File: Classfy.py
# @Function:
from CustomerClassfied.CustomerUtil import ClassifyCustomer
if __name__ == '__main__':
    #获取不同车型下的iccid
    cc = ClassifyCustomer()
    model_iccid_dict = cc.customer_classfy(2,5)
    #获取不同车型iccid每个月的流量
    for model_iccid in model_iccid_dict.items():
    #model_iccid[0]为车型，model_iccid[1]为对应车型的ICCID列表

    #获取流量分段中的人数
    #画图
# -*- coding:utf-8 -*-
# @Time: 2020/3/26 12:16
# @Author: BaLuoBooooo
# @Email: 1xxxxxxx@qq.com
# @File: DataFormat.py
# @Function:
class DateCut:
    def data_format(self,date:str):
        date_list = date.split('-')
        mouth = date_list[1]
        year = date_list[0].split("'")
        print(mouth,year)


if __name__ == '__main__':
    date = "2020-03-07 20:12:27"
    DC = DateCut()
    DC.data_format(date)


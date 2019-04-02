# coding:utf-8

import ddt
import unittest
import time
import HTMLTestReportCN
from autoSinnetCloud.tools.models import excel_to_dic

file_path = "E:\Desktop/testdata_optadd.xlsx"
file_sheet = "Sheet5"
exl = excel_to_dic.ExcelToDic(file_path, file_sheet)
data_org = exl.excel_to_dic()


def test(data):
    for x in data:
        if data[x] == "":
            print(x)
            break


if __name__ == "__main__":

    data1 = {"name": "", "age": "20", "sex": "男", "address": "wqer"}
    data2 = {"name": "Bob", "age": "", "sex": "女", "address": "wqer"}
    data3 = {"name": "Tom", "age": "20", "sex": "", "address": "wqer"}
    data4 = {"name": "Jim", "age": "20", "sex": "男", "address": ""}

    test(data3)
    test(data4)
    test(data1)
    test(data2)

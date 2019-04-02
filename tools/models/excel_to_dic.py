# coding:utf-8
import xlrd


class ExcelToDic:
    def __init__(self, file_path, file_sheetname):
        self.data = xlrd.open_workbook(file_path)
        self.table = self.data.sheet_by_name(file_sheetname)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.row_num = self.table.nrows
        # 获取总列数
        self.col_num = self.table.ncols

    def excel_to_dic(self):
        if self.row_num <= 1:
            print("总行数小于1！请检查excel中数据！")
        else:
            r = []
            j = 1
            for i in range(self.row_num - 1):
                s = {}
                values = self.table.row_values(j)
                for x in range(self.col_num):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

# if __name__ == '__main__':
#     file_path = "E:\Desktop\\testdata.xlsx"
#     file_sheetname = "Sheet1"
#     data = ExcelToDic(file_path, file_sheetname)
#     print(data.excel_to_dic())

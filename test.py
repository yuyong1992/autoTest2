# coding:utf-8


class Test:
    def prt(self):
        print(self)
        print(self)


t = Test()
# T.prt()
Test.prt(t)
# coding:utf-8

import HTMLTestReportCN
import unittest
import time
import os
# from autoTest2.cases.test_login import Login
# from autoTest2.cases.test_login import LoginErr, LoginSuccess, LinkClick
# from cases.test_opt_add import OptAddSuccess, OptAddErrSub, OptAddErrInTime, OptAddErrInTimeNull
from cases.test_dashboard import CloseTipOfLastLogin

# 以下是几种将测试用例添加到测试套件中的方法

# 添加测试用例，方法一：通过测试类查找测试用例
suit = unittest.TestSuite()
# suit.addTest(unittest.makeSuite(OptAddSuccess))
# suit.addTest(unittest.makeSuite(OptAddErrSub))
# suit.addTest(unittest.makeSuite(OptAddErrInTime))
# suit.addTest(unittest.makeSuite(OptAddErrInTimeNull))
suit.addTest(unittest.makeSuite(CloseTipOfLastLogin))

# suit.addTest(unittest.makeSuite(LeadEditSuccess))

# 添加测试用例，方法二：通过测试类查找测试用例
# suit = unittest.TestLoader().loadTestsFromTestCase(LoginErrPhone)

'''
# 添加测试用例，方法三：通过测试用例文件*py查找
path_case = os.path.join(os.getcwd(), 'cases')
suit = unittest.TestLoader().discover(path_case, pattern="test*.py", top_level_dir=None)
'''

if __name__ == '__main__':
    report_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    report_dir = os.path.dirname(os.path.abspath('.')) + r'/autoTest2/result/report/report' + report_time + r'.html'
    file = open(report_dir, 'wb')

    runner = HTMLTestReportCN.HTMLTestRunner(stream=file,
                                             title=r'Dashboard',
                                             description=r'Dashboard页面相关操作',
                                             tester='Yuyong')
    runner.run(suit)

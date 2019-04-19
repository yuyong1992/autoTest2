# _*_ coding: utf-8 _*_
import logging
import os.path
import time


class Logger(object):
    def __init__(self, logger):
        """
            指定保存日志的文件路径，日志级别，
            以及调用文件将日志存入到指定的文件中
        """

        # 创建一个logger
        self.logger = logging.getLogger(logger)

        # 如果已经存在Handler，就清理一下：解决多个文件调用logger，日志重复打印的问题
        self.logger.handlers.clear()

        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 项目根目录下/Logs保存日志
        log_path = os.path.dirname(os.path.abspath('.')) + \
            '/autoTest2/logs/'
        # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录
        # log_path = 'F:\\Code\PyCharm\\autoTest\\autoSinnetCloud\\report\logs'
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - \
            %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

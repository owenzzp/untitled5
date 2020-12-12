# coding=utf-8
'''
Created on 2016-7-26
@author: Jennifer
Project:编写Web测试用例
'''
import sys,os
sys.path.append("/root/dingdian/dingdian/")
import unittest
from HTMLTestRunner import HTMLTestRunner
import Testbaidu
import Testyoudao

#构造测试集
suite = unittest.TestSuite()
# 添加测试案例
suite.addTest(Testbaidu.BaiduTest('test_baidu'))
suite.addTest(Testyoudao.YoudaoTest('test_youdao'))

if __name__=='__main__':
    #执行测试
    runner = HTMLTestRunner(
        stream=open("测试报告.html", "wb"),
        description="测试报告",
        title="unittest练习"
    )
    # runner = unittest.TextTestRunner()
    runner.run(suite)



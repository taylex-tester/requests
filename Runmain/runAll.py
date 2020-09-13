import unittest
<<<<<<< HEAD
from Common import HTMLTestRunner
=======
from HTMLTestRunner import HTMLTestRunner
>>>>>>> 3844286a40da226ec37809448b36ca460b06ee04
from Util.basePath import os, base_path
from Common.sendEmail import sendEmail
from Common.logger import Logger

log = Logger().get_logger("debug")


class Run(object):
    def __init__(self):
        self.case_path = os.path.join(base_path, "TestCase")
        self.report_path = os.path.join(base_path, "Report", "report.html")
        log.info("case_path--->", self.case_path)
        log.info("report_path--->", self.report_path)

    def run(self):
        discover = unittest.defaultTestLoader.discover(self.case_path)
        log.info("case_list--->", discover)
        try:
            with open(self.report_path, "wb") as f:
                runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                                       title="TEST",
                                                       description="This is test!")
                runner.run(discover)
        except Exception as b:
            print("测试失败！！！", b)
        try:
            sendEmail(
                title="TEST REPORT",
                desc="THIS IS TEST",
                reve=["1163386702@qq.com"],
                filename="report.html"
            )
        except Exception as a:
            print("发送失败", a)

        print("测试结束,测试结果已发送至同事")


if __name__ == '__main__':
    Run().run()

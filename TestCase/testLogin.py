import json
import os
import ddt
import unittest
from HTMLTestRunner import HTMLTestRunner
from Util.basePath import base_path
from Util.readExcel import readExcel
from Util.sendRequest import request
from Common.readConfig import readConfig

test_data = readExcel.excel_list()
host = readConfig.get_cfg_value("server", "host")


@ddt.ddt
class TestCase01(unittest.TestCase):
    @ddt.data(*test_data)
    def test01(self, data):
        path = data[1]
        self.url = host + path
        self.caseId = data[0]
        self.method = data[2]
        self.edata = json.loads(data[3])
        self.expect = data[4]
        self.result = data[5]
        self.log = data[6]
        self.execute()

    def execute(self):
        # 仅对响应json文本断言
        response = request.send_main(method=self.method, url=self.url, data=self.edata)
        msg = response.json().get("message")
        self.assertEqual(msg, self.expect)
        # 断言成功后回写PASS
        row = readExcel.get_row_number(self.caseId)
        readExcel.write(row, 6, "PASS")


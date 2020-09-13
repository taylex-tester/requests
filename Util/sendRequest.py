import requests


class SendRequest(object):
    @staticmethod
    def _send_get(url, data):
        res = requests.get(url=url, params=data)
        return res

    @staticmethod
    def _send_post(url, data):
        res = requests.post(url=url, data=data)
        return res

    def send_main(self, method, url, data):
        if method == "GET":
            res = self._send_get(url, data)
        elif method == "POST":
            res = self._send_post(url, data)
        else:
            raise Exception("methodError")
        return res


request = SendRequest()
# if __name__ == '__main__':
#     from Common.readConfig import readConfig
#     b = readConfig.get_cfg_value("server", "host")
#     a = SendRequest()
#     data = {"name": "taylex"}
#     res = a.send_main("POST", b + 'post', data)
#     print(res.text)
#     print(res.url)


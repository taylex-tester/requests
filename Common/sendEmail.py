import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from Common.readConfig import readConfig
from Util.basePath import base_path


class SendEmail(object):
    def __init__(self):
        section = "Email"
        get = readConfig.get_cfg_value
        self.host = get(section, "host")
        self.username = get(section, "username")
        self.password = get(section, "password")
        self.port = 25
        self.ssl_port = 465

    def send(self, title, desc, reve, filename=None):
        msg = MIMEMultipart()
        # 设置主题
        msg["Subject"] = title
        msg["From"] = self.username
        msg["To"] = ",".join(reve)

        # 描述部分
        part1 = MIMEText(desc)
        msg.attach(part1)

        # 附件部分
        if filename:
            file_path = os.path.join(base_path, "Report", filename)
            with open(file_path, 'rb') as f:
                data = f.read()
            # 文件名如果含有中文,需要base64编码
            # filename = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
            part2 = MIMEApplication(data)
            part2.add_header("Content-Disposition", "attachment", filename=filename)
            msg.attach(part2)

        smtp = smtplib.SMTP_SSL(self.host, self.ssl_port)
        smtp.login(self.username, self.password)
        smtp.sendmail(self.username, reve, msg.as_string())

        smtp.close()


sendEmail = SendEmail().send

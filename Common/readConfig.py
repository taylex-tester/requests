import configparser
import os
from Util.basePath import base_path


class ReadConfig(object):
    @staticmethod
    def _load_cfg():
        """
        加载配置文件
        :return:
        """
        # 获取配置文件路径
        config_path = os.path.join(base_path, "Config", "config.ini")
        cfg = configparser.ConfigParser()
        cfg.read(config_path, encoding="UTF-8")
        return cfg

    def get_cfg_value(self, section, option):
        """
        获取配置文件的值
        :param section:
        :param option:
        :return:
        """
        cfg = self._load_cfg()
        value = cfg.get(section=section, option=option)
        return value


readConfig = ReadConfig()

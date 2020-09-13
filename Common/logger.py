import logging

from Util.basePath import base_path, os
from logging.handlers import TimedRotatingFileHandler


class Logger(object):
    level = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }

    def __init__(self, log_name="test_log"):
        self.logger = logging.Logger(log_name)
        logging.root.setLevel(logging.DEBUG)
        ftm = "%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s - %(message)s"
        self.ftm = logging.Formatter(ftm)

    def get_logger(self, file_level, filename="test.log"):
        if not self.logger.handlers:
            console = logging.StreamHandler()
            console.setLevel(logging.WARNING)
            console.setFormatter(self.ftm)
            self.logger.addHandler(console)

            file_path = os.path.join(base_path, "Report", filename)
            log_file = TimedRotatingFileHandler(file_path,
                                                when="D",
                                                backupCount=4,
                                                encoding="UTF-8")
            get_level = self.level.get(file_level)
            log_file.setLevel(get_level)
            log_file.setFormatter(self.ftm)
            self.logger.addHandler(log_file)
        return self.logger



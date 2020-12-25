# -*- encoding : utf-8 -*-
"""
@File       : logrecord.py
@Time       :2020/12/21 15:20
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from oslo_log import log as logging
import time


LOG = logging.getLogger(__name__)


def record(fn):
    def logrecord(*args):
        print("{}:------{} with {} runs".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), fn, str(args)))
        LOG.info("{}:------{} with {} runs".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), fn, str(args)))
        return fn(*args)
    return logrecord


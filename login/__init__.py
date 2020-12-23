# -*- encoding : utf-8 -*-
"""
@File       : __init__.py.py
@Time       :2020/12/22 16:58
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from oslo_config import cfg

CONF = cfg.CONF
cfg_group = cfg.OptGroup(name="DEFAULT", title="DEFAULT")
cfg_opts = [
    cfg.StrOpt(name='username', default='root', help="mysql username"),
    cfg.StrOpt(name='password', default='root', help="mysql password")
]
CONF.register_group(cfg_group)
CONF.register_opts(cfg_opts, cfg_group)


def loginauth(path, username, password):
    name = cfg.CONF.DEFAULT.username
    pwd = cfg.CONF.DEFAULT.password

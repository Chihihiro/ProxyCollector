# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019年09月03日 14:29:25
# @Author  : Joyce
# @Project : ProxyCollector
# @File    : ConnectDataBase.py
# @Software: PyCharm
# @Describe:
import logging
import pymysql
from setting import DATABASE


class ConnectMySQL(object):
    def __init__(self):
        # 连接MySQL数据库
        self.DBINFO = DATABASE
        self.connect = pymysql.connect(
            DATABASE["HOST"],
            DATABASE["USER"],
            DATABASE["PASSWORD"],
            DATABASE["DB"],
            DATABASE["PORT"]
        )
        self.cursor = self.connect.cursor()

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    @staticmethod
    def log(info):
        result = [f"{key}: {info[key]}" for key in info]
        return "{\n\t"+"\n\t".join(result)+"\n}"

    # 写入数据
    def insert(self, table, value):
        sql = f"INSERT INTO `{table}`(`PROTOCOL`, `HOST`, `PORT`, `SPEED`, `UPDATETIME`) VALUE{value};"
        try:
            self.cursor.execute(sql)
        except pymysql.err.IntegrityError:
            self.connect.rollback()
        else:
            self.connect.commit()
            title = ("PROTOCOL", "HOST", "PORT", "SPEED", "UPDATE_TIME")
            logging.debug(f"Data was successfully written to the database.  \n{self.log(dict(zip(title, value)))}")

    # 查询数据
    def select(self):
        sql = "SELECT `protocol`,`host`,`port` FROM pool WHERE isActive=1;"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result if result else []

    # 禁用已失效的代理ip
    def update(self, host, port):
        sql = f"UPDATE pool SET isActive=0 WHERE `host`='{host}' and `port`={port};"
        self.cursor.execute(sql)
        self.connect.commit()
        logging.info(f"IP ({host}:{port}) is invalid. This IP will be disabled")


ConnectMySQL()

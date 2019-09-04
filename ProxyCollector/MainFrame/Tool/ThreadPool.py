# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019年09月03日 13:51:20
# @Author  : Joyce
# @Project : ProxyCollector
# @File    : ThreadPool.py
# @Software: PyCharm
# @Describe: 

from queue import Queue
from threading import Thread


class ThreadPool(object):  # 创建线程池类
    def __init__(self, max_num=20):  # 默认最大长度为20的队列
        self.queue = Queue(max_num)  # 创建一个队列
        for i in range(max_num):  # 循环把线程对象加入到队列中
            self.queue.put(Thread)  # 把线程的类名放进去，执行完这个Queue

    def get_thread(self):  # 定义方法从队列里获取线程
        return self.queue.get()  # 在队列中获取值

    def add_thread(self):  # 线程执行完任务后，在队列里添加线程
        thread = self.queue.put(Thread)
        return thread










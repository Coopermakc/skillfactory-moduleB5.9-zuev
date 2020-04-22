#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:57:11 2020

@author: macbook
"""
import time
from contextlib import ContextDecorator
from random import random

#класс декоратора с возможностью использования как контекстного менеджера
class Timer(ContextDecorator):

    def __init__(self,num_runs):
        self.num_runs = num_runs

    def __call__(self,func):
        def inner_function(args):
            avg_time = 0
            for _ in range(self.num_runs):
                t0=time.time()
                func(args)
                t1=time.time()
                avg_time += (t1-t0)
                avg_time /= self.num_runs
            return "Time %.5f" %avg_time
        return inner_function

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return self

#обычный декоратор
def time_this(num_runs):
    def decorator(func):
        def wrap(param):
            avg_time = 0
            for _ in range(num_runs):
                t0=time.time()
                func(param)
                t1=time.time()
                avg_time += (t1-t0)
            avg_time /= num_runs
            return "Time %.5f" %avg_time
        return wrap
    return decorator

@Timer(10)
def f(n):
   for j in range(n):
        pass

with Timer(10):
    print(f(1000000))

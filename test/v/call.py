# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:40:06 2016

@author: frank
"""
class account:
    def __init__(self, name, num, year):
        self.name = name
        self.num = num
        self.year = year
    def nameReturn(self):
        return self.name
    def plusNum(self, val):
        self.num += val
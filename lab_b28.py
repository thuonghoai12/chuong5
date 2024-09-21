# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:06:09 2024

@author: thuonghoai
"""
n = int(input("Nhập số nguyên dương N = "))
so = []
while n < 0:
    n = int(input("Nhập lại số nguyên dương N = "))
for i in range(n, 1 + n):
    so += [i]
print(so)
    

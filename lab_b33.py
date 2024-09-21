# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:14:48 2024

@author: thuonghoai
"""
n = int(input("Nhập số nguyên dương N = "))
while n <= 0:
    n = int(input("Nhập lại số nguyên dương N = "))
for i in range(1, 1 + n):
    if i * i == n:
        print("N là số chính phương")
        break
else:
    print("N không là số chính phương")

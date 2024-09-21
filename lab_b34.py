# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:30:34 2024

@author: thuonghoai
"""
n = int(input("Nhập số nguyên dương N = "))
while n <= 0:
    n = int(input("Nhập lại N = "))
for i in range(2, n):
    if n % i == 0:
        print(n, "không là số nguyên tố")
        break
else:
    print(n, "là số nguyên tố")

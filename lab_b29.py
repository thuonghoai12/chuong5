# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:42:10 2024

@author: thuonghoai
"""
n = int(input("Nhập số nguyên dương N = "))
tong = 0
while n < 0:
    n = int(input("Nhập lại số nguyên dương N = "))
for so in str(n):
    tong += int(so)
print("Tổng các chữ số N =", tong)
    

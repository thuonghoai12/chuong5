# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:59:58 2024

@author: thuonghoai
"""
n = int(input("Nhập số n lẻ để tính biểu thức S = 1 * 2 * 3 *...* n: "))
while n <= 0 or n % 2 == 0:
    n = int(input("Nhập lại n là số lẻ: "))
kq = 1
for i in range(1, n+1):
    kq = kq * i
print("Kết quả S = ", kq)
    

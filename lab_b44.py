# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 02:22:41 2024

@author: thuonghoai
"""
n = int(input("Nhập n để tín biểu thức S = (1/2 + 3/4 + ... + (2n+1)/(2n+2): "))
while n <= 0:
    n = int(input("Nhập lại n là số nguyên dương: "))
kq = 0
for i in range (0, n + 1):
    kq += ((2*i)+1) / ((2*i)+2)
print("Kết quả S =", kq)
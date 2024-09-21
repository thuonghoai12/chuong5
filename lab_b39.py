# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 01:09:55 2024

@author: thuonghoai
"""
n = int(input("Nhập n để tính biểu thức S = 1 + 1/2 + 1/3 +...+1/n: "))
while n <= 0:
    n = int(input("Nhập lại n là số nguyên dương: "))
kq = 0
for i in range(1, 1+n):
    kq += 1/i
print("Kết quả S =", kq)
    

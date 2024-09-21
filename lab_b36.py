# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:41:11 2024

@author: thuonghoai
"""
n = int(input("Nhập n để tính biểu thức S = 1^2 + 2^2 + 3^2 +...+ n^2: "))
kq = 0
while n <= 0:
    n = int(input("Nhập lại n: "))
for i in range(1, 1 + n):
    kq += i ** 2
print("Kết quả S =", kq)
    

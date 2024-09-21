# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:44:55 2024

@author: thuonghoai
"""
n = int(input("Nhập n chẵn để tính biểu thức S = 2 + 4 + 6 +...+ n: "))
kq = 0
while n <= 0 or n % 2 != 0:
    n = int(input("Nhập lại n là số chẵn: "))
for i in range(2, n + 1, 2):
    kq += i
print("Kết quả S =", kq)
    


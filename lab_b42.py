# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 02:14:10 2024

@author: thuonghoai
"""
n = int(input("Nhập n để tính biểu thức S = 1/(1*2) + 1/(2*3) +...+ 1/(n*(n+1)): "))
while n <= 0:
    n = int(input("Nhập lại n: "))
kq = 0
for i in range(1, n+1):
    kq += 1/(i*(i+1))
print("Kết quả S =", kq)
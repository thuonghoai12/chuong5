# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 01:28:07 2024

@author: thuonghoai
"""
n = int(input("Nhập n để tính biểu thức S = 1 + 1/3 + 1/5 +...+ 1/(2n+1): "))
while n <= 0:
    n = int(input("Nhập lại n: "))
kq = 0
for i in range(0, n+1):
    kq += 1/((2*i)+1)
print("Kết quả S =", kq)
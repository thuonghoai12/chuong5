# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 01:13:53 2024

@author: thuonghoai
"""
n = int(input("Nhập n để tính biểu thức S = 1/2 + 1/4 +...+ 1/2n: "))
while n <= 0:
    n = int(input("Nhập lại số nguyên dương n: "))
kq = 0
for i in range(1, 1+n):
    kq += 1/(2*i)
print("Kết quả S =", kq)

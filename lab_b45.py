# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 02:25:26 2024

@author: thuonghoai
"""
print("S = x + (x^2)/(1+2) + (x^3)/(1+2+3) ... + (x^n)/(1+2+3+...+n)")
x = float(input("Nhập x= "))
n = int(input("Nhập n= "))
while n <= 0:
    n = int(input("Nhập lại n là số nguyên dương: "))
kq = 0
so_n = 0
for i in range (1, n+1):
    so_n += i
    kq += (x**i) / so_n
print("Kết quả là: ", round(kq, 2))

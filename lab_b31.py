# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:22:31 2024

@author: thuonghoai
"""
a = int(input("Nhập cạnh a = "))
b = int(input("Nhập cạnh b = "))
c = int(input("Nhập cạnh c = "))
while a <= 0 or b <= 0 or c <= 0:
    if a <= 0:
        a = int(input("Nhập lại cạnh a = "))
    if b <= 0:
        b = int(input("Nhập lại cạnh b = "))
    if c <= 0:
        c = int(input("Nhập lại cạnh c = "))
if a + b > c or a + c > b or b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif a == b != c or a == c != b or b == c != a:
        print("Tam giác cân")
    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        print("Tam giác vuông")
    elif (a == b and a ** 2 + b ** 2 == c ** 2) or \
        (a == c and a ** 2 + c ** 2 == b ** 2) or \
        (b == c and b ** 2 + c ** 2 == a ** 2):
        print("Tam giác vuông cân")
    else:
        print("Tam giác thường")
else:
    print("Nhập lại. Đây không phải là 1 tam giác")
         


       



# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 02:54:56 2024

@author: thuonghoai
"""
so = float(input("Nhập số từ [-99, 99]: "))
while so < -99 or so > 99:
    print("Số bạn nhập không hợp lệ. Vui lòng nhập lại!")
    so = float(input("Nhập lại số từ [-99, 99] thôi: "))
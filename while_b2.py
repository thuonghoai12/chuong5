# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 03:03:59 2024

@author: thuonghoai
"""
so = float(input("Nhập số từ [-89.9, 88.8]: "))
while so < -89.9 or so > 88.8:
    print("Số bạn nhập không hợp lệ. Vui lòng nhập lại!")
    so = float(input("Nhập lại số từ [-89.9,88.8] thôi: "))

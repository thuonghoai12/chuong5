# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 02:04:43 2024

@author: thuonghoai
"""
n = int(input("Chọn bảng cửu chương từ 2 đến 9: "))
if n < 1 or n > 9:
    print("Không hợp lệ")
else:
    for i in range(1, 10):
        print("{} x {} = {}".format(n, i, n * i))

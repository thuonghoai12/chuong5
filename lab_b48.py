# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 02:38:30 2024

@author: thuonghoai
"""
print("Liệt kê tất cả bộ nghiệm nguyên của: 2x + 7y + 9z = 979 (x, y, z > 0) và (x + y + z) nhỏ nhất")
TNN = 979
for x in range(1, 483):
    for y in range(1, 140):
        for z in range(1, 109):         
            if 2*x + 7*y + 9*z == 979:
                tong = x + y + z
                if tong < TNN:  
                    TNN = tong
                    so_nho_nhat = [x, y, z]
print("Bộ nghiệm có tổng các nghiệm lớn nhất là", so_nho_nhat,"với tổng =", TNN)

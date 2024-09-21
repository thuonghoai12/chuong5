# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 03:14:04 2024

@author: thuonghoai
"""
danhsach = [i for i in range(2020, 3838) if i % 2 == 0]
danhsach_moi = [j for j in danhsach if j % 9 == 0]
for k in danhsach_moi:
    print(k, end="\t")
    
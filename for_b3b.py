# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 02:45:37 2024

@author: thuonghoai
"""
import random
so = 0 
for i in range(random.randrange(1, 20)):
    sothuc = random.uniform(18, 99)
    so += 1
    binhphuong = sothuc ** 2
    print(so,"\u00B2 = ", binhphuong, end=",\t")
print(f"\n Có tất cả {so} số bình phương")

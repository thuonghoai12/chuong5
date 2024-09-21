# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 02:31:26 2024

@author: thuonghoai
"""
import random
so = 0
for i in range(random.randrange(1, 50)):
    dem = random.randrange(20, 31)
    print(dem, end='\t')
    so += 1
print("\nSố lượng phần tử: ", so)

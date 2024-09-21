# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 02:29:19 2024

@author: thuonghoai
"""
print("Liệt kê bộ nghiệm nguyên của: 2x + 7y + 9z = 979 với (x, y, z > 0)")
for x in range(1, 483):
    for y in range(1, 140):
        for z in range(1, 109):
            if 2*x + 7*y + 9*z == 979:
                print([x, y, z], end='\t')

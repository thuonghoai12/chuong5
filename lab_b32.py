# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:08:41 2024

@author: thuonghoai
"""
d = int(input("Nhập quãng đường taxi đi(km):"))
money = 0
for km in range(1, d + 1):
    if km <= 1:
        money += 15000
    elif 2 <= km <= 5:
        money += 13500
    elif km >= 6:
        money += 11000
if d > 120:
    money = money * 0.9
print(f"Tiền phải thanh toán là {money} vnd")
        
        
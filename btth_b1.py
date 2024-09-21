# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:11:01 2024

@author: thuonghoai
"""
chuoi = input("Nhập vào một chuỗi: ")
ktdb = '@ # $ % ^ & * ( ) - = + . /'
chuoi_ktdb = [i for i in chuoi if i in ktdb]
print(len(chuoi_ktdb))
print(chuoi_ktdb)

ktct = [j for j in chuoi if j.islower()]
print(len(ktct))
print(ktct)

kts = [k for k in chuoi if k.isdigit()]
print(len(kts))
print(kts)

ktch = [e for e in chuoi if e.isupper()]
print(len(ktch))
print(ktch)


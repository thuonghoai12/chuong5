# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:13:45 2024

@author: thuonghoai
"""
time = input("Nhập ngày tháng năm (dd/mm/yyyy): ")
dd, mm, yyyy = time.split('/')
ngay = int(dd)
thang = int(mm)
nam = int(yyyy)
namnhuan = (nam % 400 == 0) or (nam % 4 == 0 or nam % 100 != 0)
if thang == 2:
    if namnhuan:
        print(f"Tháng {thang} có 29 ngày")
    else:
        print(f"Tháng {thang} có 28 ngày")
elif thang in [4, 6, 9, 11]:
    print(f"Tháng {thang} có 31 ngày")
else:
    print(f"Tháng {thang} có 30 ngày")

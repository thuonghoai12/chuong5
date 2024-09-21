# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:49:14 2024

@author: thuonghoai
"""
email = input("Nhập địa chỉ email: ")
if email.count('@') != 1:
    print("Email không hợp lệ")
else:
    ten, duoi = email.split('@')
    if len(ten) < 6:
        print("Email không hợp lệ (Phần trước @ phải có tối thiểu 6 ký tự).")
    else:
        whitespace = True
        kytu = True
        for i in ten:
            if i == ' ':
                whitespace = False
            elif not i.isalnum():
                kytu = False
        if whitespace == False:
            print("Email không hợp lệ (Phần trước @ chứa khoảng trắng).")
        if kytu == False:
            print("Email không hợp lệ (Phần trước @ chứa ký tự đặc biệt).")


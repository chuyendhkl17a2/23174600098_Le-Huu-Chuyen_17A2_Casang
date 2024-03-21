so_luong_nguoi=float(input("Nhap vao so luong nguoi mua ve :"))
if so_luong_nguoi==1:
    print("Gia ve cho mot nguoi la : 120000vnđ")
elif so_luong_nguoi>=2 and so_luong_nguoi <=4:
    so_tien= (so_luong_nguoi*120000)*0.95 
    print("Gia ve cua cac ban la : ",so_tien)
elif so_luong_nguoi >=4 and so_luong_nguoi<=10:
    so_tien=(so_luong_nguoi*120000)*0.9
    print("Gia ve cua cac ban la : ",so_tien)
elif so_luong_nguoi >=10:
    so_tien=(so_luong_nguoi*120000)*0.8
    print("Gia ve cua cac ban la : ",so_tien)    

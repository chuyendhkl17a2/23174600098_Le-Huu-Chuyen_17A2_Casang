a=int(input("Nhap vao mot so nguyen :"))
if a>=1000:
    so_hang_nghin=(a//1000)%10
    print("So hang nghin cua so da nhap la:",so_hang_nghin)
else:
     print("So hang nghin cua so vua nhap la : 0")
x=float(input("Nhap vao he so goc :"))
y=float(input("Nhap vao he so tu do:"))
I1,I2=map(float,input("nhap vao toa do tam i:").split())
ban_kinh=float(input("nhap vao ban kinh r:"))
# khoảng cách từ đường thẳng đến tâm đường tròn
D=abs(x*I1-I2+y)/((x**2+1)**0.5)
if D>ban_kinh:
    print("Đường thẳng nằm ngoài hình tròn")
elif D<ban_kinh:
    print("Đường thẳng cắt đường tròn")
elif D==ban_kinh:
    print("Đường thẳng tiếp xúc đường tròn")
else:
    print("đường thẳng nằm trog đường tròn")      
    
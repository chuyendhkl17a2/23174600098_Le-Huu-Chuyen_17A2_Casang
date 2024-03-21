a=int(input("Nhap vao cac so nguyen duong a : "))
b=int(input("Nhap vao cac so nguyen duong b : "))
c=int(input("Nhap vao cac so nguyen duong c : "))
if a>b>c or a<b<c :
    print(b,"la so lon thu 2")
elif b>a>c or b<a<c:
    print(a,"la so lon thu 2")
else:
    print(c,"la so lon thu 2")        
 

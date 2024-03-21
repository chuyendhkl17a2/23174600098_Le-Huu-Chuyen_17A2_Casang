a=float(input("Nhap vao he so a : "))
b=float(input("nhap vao he so b :"))
def giai_phuong_trinh_bac_nhat(a,b):
    if a==0 and b==0:
     print("Phuong trinh vo so nghiem")
    elif a==0 and b!=0:
        print("Phuong trinh vo nghiem")
    else:
       x=-b/a    
       print("Nghiem cua phuong trinh la:",x)
giai_phuong_trinh_bac_nhat(a,b)
          

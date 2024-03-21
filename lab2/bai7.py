chieu_cao=float(input("Nhap vao chieu cao cua ban :"))
can_nang=float(input("Nhap vao can nang cua ban :"))
BMI=can_nang/chieu_cao**2
if BMI <18.5 :
    print("Phan loai BMI: bạn hơi Gầy")
elif BMI>=18.5 and BMI<=24.9:
    print("Phan loai BMI: bạn Bình thường")
elif BMI>=25 and BMI <=29.9:
    print("Phan loai BMI:bạn Hơi béo một xíu")
else:
    print("Phan loai BMI: bạn Béo mất rồi")
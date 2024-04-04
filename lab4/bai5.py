import math
while True:
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    print("1.phép TÍnh tổng")
    print("2.phép tính hiệu")
    print("3.phép tính tích")
    print("4.phép tính thương")
    print("5.phép tính Lũy thừa")
    print("6.phép tính Căn bậc hai")
    chon_phep_tinh = int(input("Nhập lựa chọn của bạn (1-6): "))

    # Thực hiện phép tính tương ứng và in ra kết quả
    if chon_phep_tinh == 1:
        print("Tổng =", a + b)
    elif chon_phep_tinh == 2:
        print("Hiệu =", a - b)
    elif chon_phep_tinh == 3:
        print("Tích =", a * b)
    elif chon_phep_tinh== 4:
        if b == 0:
            print("Không thể chia cho số 0")
        else:
            print("Thương =", a / b)
    elif chon_phep_tinh == 5:
        print("Lũy thừa =", a ** b)
    elif chon_phep_tinh == 6:
        if a < 0:
            print("Không thể tính căn bậc hai của số âm")
        else:
            print("Căn bậc hai của số thứ nhất =", math.sqrt(a))
        if b < 0:
            print("Không thể tính căn bậc hai của số âm")
        else:
            print("Căn bậc hai của số thứ hai =", math.sqrt(b))
    else:
        print("Lựa chọn không hợp lệ")

    # Hỏi người dùng có muốn tiếp tục không
    tiep_tuc = input("Bạn có muốn tiếp tục không ạ(có or không) : ")
    if tiep_tuc != 'có':
        break
  
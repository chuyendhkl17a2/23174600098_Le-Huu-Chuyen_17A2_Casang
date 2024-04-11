string = input("Nhập chuỗi ký tự: ")
if len(string) > 10:
    string1 = string[1:8]
    print("a) Chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8:", string1)
    string2 = string[4:9]
    print("b) Chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5:", string2)
    string3 =string[-3:]
    print("c) Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", string3)
    string4 = string.lower()
    print("d) Chuỗi sau khi chuyển đổi thành chữ thường:",string4)
    string5 = string.upper()
    print("e) Chuỗi sau khi chuyển đổi thành chữ hoa:", string5)
    string6 = string[::-1]
    print("f) Chuỗi sau khi đảo ngược:", string6)
else:
    print("Nhập lại hơn 10 kí tự")


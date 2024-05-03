kho = {
 "banana": 6,
 "apple": 5,
 "orange": 32,
 "pear": 15
}

gia_tien = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3
}

mua_hang = {
    "banana": 2,
    "apple": 3,
    "orange": 5,
    "pear": 2
}

hoa_don = {}
tong_tien = 0

print("Hóa đơn mua hàng:")
for mat_hang, so_luong in mua_hang.items():
    if mat_hang in kho and mat_hang in gia_tien:
        don_gia = gia_tien[mat_hang]
        if kho[mat_hang] >= so_luong:
            kho[mat_hang] -= so_luong
            thanh_tien = don_gia * so_luong
            hoa_don[mat_hang] = {
                "So luong": so_luong,
                "Don gia": don_gia,
                "Thanh tien": thanh_tien
            }
            tong_tien += thanh_tien
            print(f"Mặt hàng: {mat_hang}, Số lượng: {so_luong}, Đơn giá: {don_gia}, Thành tiền: {thanh_tien}")
        else:
            print(f"Không đủ hàng cho mặt hàng '{mat_hang}'")
    else:
        print(f"Mặt hàng '{mat_hang}' không có trong kho hoặc không có giá")

print(f"Tổng số tiền của hóa đơn: {tong_tien}")

print("\nSố lượng của các mặt hàng trong kho sau khi bán:")
for mat_hang, so_luong in kho.items():
    print(f"{mat_hang}: {so_luong}")
N = int(input("Nhập số nguyên N: "))

# Tạo từ điển và in ra từ điển
LE_HUU_CHUYEN = {}
for x in range(1, N + 1):
    LE_HUU_CHUYEN[x] = x ** 3

print("Từ điển:")
print(LE_HUU_CHUYEN)
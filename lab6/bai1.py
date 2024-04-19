n = int(input("Nhập số phần tử của mảng: "))
mang = []
print("Nhập các phần tử của mảng:")
for i in range(n):
        mang.append(int(input()))
tong_chan = sum([num for num in mang if num % 2 == 0])
tong_le = sum([num for num in mang if num % 2 != 0])
print("Tổng các số chẵn trong mảng là:", tong_chan)
print("Tổng các số lẻ trong mảng là:", tong_le)
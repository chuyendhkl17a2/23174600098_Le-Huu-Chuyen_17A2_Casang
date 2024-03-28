n = int(input("Nhập vào chiều cao của tam giác: "))
a = int(input("Nhập vào số hàng: "))
b = int(input("Nhập vào số cột: "))
for i in range(1, n+1):
    # In ra khoảng trắng của mỗi dòng
    for j in range(n - i):
        print(' ', end="")
    # In ra ký tự * cho tam giác
    for j in range(i):
        print("* ", end ='')
    # Xuống dòng
    print()

for i in range(1,a+1):
    for j in range(1,b+1):
        print("* ", end ='')
    print() 
# hình 1
print("     *  ")
print("    * *  ")
print("   * * *  ")
print("  * * * *  ")
print(" * * * * * ")
print(" * * * * *  ")
print("  * * * *  ")
print("   * * *  ")
print("    * *  ")
print("     *  ")       

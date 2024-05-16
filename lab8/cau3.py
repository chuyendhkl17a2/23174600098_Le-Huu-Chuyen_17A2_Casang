def cubesum(n):
    return sum(int(digit) ** 3 for digit in str(n))

def isArmstrong(n):
    return n == cubesum(n)

def PrintArmstrong():
    print("Các số Armstrong là:")
    for i in range(1, 1000):  # Kiểm tra các số từ 1 đến 999
        if isArmstrong(i):
            print(i)

PrintArmstrong()
n = int(input("Nhập số Fibonacci cần tạo: "))
fibonacci= [0, 1] + [fibonacci[i-1] + fibonacci[i-2] for i in range(2, n)]
numbers = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
print("Dãy Fibonacci gồm", n, "số đầu tiên là:", fibonacci)
print("Danh sách các số nguyên tố nhỏ hơn 100 là:", numbers)
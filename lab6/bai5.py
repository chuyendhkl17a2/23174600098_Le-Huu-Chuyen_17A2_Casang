n= input("Nhập dãy số nguyên, cách nhau bằng dấu cách: ").split()
numbers = [int(num) for num in n]
is_prime = True
difference = numbers[1] - numbers[0]
for i in range(2, len(numbers)):
        if numbers[i] - numbers[i-1] != difference:
            is_prime = False
            break

    # In ra kết quả
if is_prime:
        print("Dãy số", numbers, "tạo thành cấp số cộng.")
else:
        print("Dãy số", numbers, "không tạo thành cấp số cộng.")

#loc số lẻ
def filter_odd_numbers(lst):
    return list(filter(lambda x: x % 2 != 0, lst))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter_odd_numbers(numbers)
print(f"Các số lẻ trong danh sách là: {odd_numbers}")
#lọc số chẵn
def filter_even_numbers(lst):
    return list(filter(lambda x: x % 2 == 0, lst))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print(f"Các số chẵn trong danh sách là: {even_numbers}")
#sử dụng hàm map() để tạo ra một danh sách
def cube_numbers(lst):
    return list(map(lambda x: x**3, lst))
numbers = [1, 2, 3, 4, 5]
cubed_numbers = cube_numbers(numbers)
print(cubed_numbers)
#các phần tử là lập phương của các số chẵn trong một danh sách
def cube_even_numbers(lst):
    return list(filter(None, map(lambda x: x**3 if x % 2 == 0 else None, lst)))
numbers = [1, 2, 3, 4, 5, 6]
cubed_even_numbers = cube_even_numbers(numbers)
print(f"Lập phương của các số chẵn trong danh sách là: {cubed_even_numbers}")
#Tạo ra một danh sách trong đó các phần tử là bình phương của các số lẻ trong một danh sách đã cho:
def square_odd_numbers(lst):
    return list(filter(None, map(lambda x: x**2 if x % 2 != 0 else None, lst)))
numbers = [1, 2, 3, 4, 5, 6]
squared_odd_numbers = square_odd_numbers(numbers)
print(f"Bình phương của các số lẻ trong danh sách là: {squared_odd_numbers}")
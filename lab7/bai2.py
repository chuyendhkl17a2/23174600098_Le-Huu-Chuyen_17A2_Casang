sinh_vien = []
for i in range(1, 11):
    ten = input(f"Nhập tên của sinh viên {i}: ")
    diem = float(input(f"Nhập điểm của sinh viên {i}: "))
    sinh_vien.append((ten, diem))
xep_loai_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for ten, diem in sinh_vien:
    if diem < 4.0:
        xep_loai_count['F'] += 1
    elif 4.0 <= diem < 5.5:
        xep_loai_count['D'] += 1
    elif 5.5 <= diem < 7.0:
        xep_loai_count['C'] += 1
    elif 7.0 <= diem < 8.5:
        xep_loai_count['B'] += 1
    else:
        xep_loai_count['A'] += 1
print("Số lượng sinh viên ở mỗi loại học lực:")
for xep_loai, count in xep_loai_count.items():
    print(f"{xep_loai}: {count} sinh viên")
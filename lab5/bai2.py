str1=input("Nhập vào kí tự chuỗi 1: ")
str2=input("Nhập vào kí tự chuỗi 2: ")
chuoi_con=""
for i in range(len(str1)):
    for j in range(len(str1),i-len(chuoi_con),-1):
        if str1[i:j] in str2 and len(str1[i:j])> len(chuoi_con):
            chuoi_con=str1[i:j]
print("Chuỗi kí tự con có độ dài ngắn nhất là :",chuoi_con)            

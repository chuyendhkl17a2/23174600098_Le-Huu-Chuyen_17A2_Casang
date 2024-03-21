print("Các thể loại phim chúng tôi có là : Hành động  ,Kinh di , Tình cảm , Hài hước , Hoạt hình")
print("Thời gian xem phim của chúng tôi là : Sáng , Trưa , Chiều , Tối")
Loai_phim=input("Mời bạn nhập loại phim cần tìm(Hành động,Kinh dị,Tình cảm,Hài hước,Hoạt hình) :")
Thoi_gian=input("Mời bạn nhập thời gian xem phim(Sáng,trưa,chiều,tối) :")
if Loai_phim=="Hành động" and (Thoi_gian=="Sáng"or Thoi_gian=="Trưa"or Thoi_gian=="Chiều"or Thoi_gian=="Tối"):
      print("""Phim được chiếu vào lúc  Sáng:7:00am đến 8:00am
                                       Trưa:11:00am đến 12:00am
                                       Chiều:1:00pm đến 1:00pm
                                       Tối:7:00pm đến 9:00pm """)
elif Loai_phim=="Hài hước" and (Thoi_gian=="Sáng"or Thoi_gian=="Trưa"or Thoi_gian=="Chiều"or Thoi_gian=="Tối"):
      print("""Phim được chiếu vào lúc Sáng:7:00am đến 8:00am
                                       Trưa:11:00am đến 12:00am
                                       Chiều:1:00pm đến 1:00pm
                                       Tối:7:00pm đến 9:00pm """)
elif Loai_phim == "Tình cảm" and Thoi_gian=="Tối":  
         print("Phim được chiếu vào buổi tối lúc 19:00pm đến 21:00pm")
elif Loai_phim=="Hoạt hình"and Thoi_gian=="Sáng":
    print("Phim tình cảm được chiếu vào buổi sáng lúc 7:00am đến 9:00am ")
elif Loai_phim=="Hoạt hình"and Thoi_gian=="Trưa":
      print("Phim được chiếu vào buổi trưa lúc 11:00am đến 12:00am ")       
elif Loai_phim=="Kinh dị" and Thoi_gian=="Tối":
      print("Phim được chiếu vào buổi tối lúc 21:00pm đến 22:00pm ") 
else:
      print("Khong có suất chiếu")          

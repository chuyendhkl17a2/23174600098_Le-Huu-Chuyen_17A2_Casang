#Số tiền sau 5 năm là
amount_after_5_years=10000*(1+0.06)*5
#số tiền sau 10 năm là
amount_after_10_years=10000*(1+0.06)*10
#tỷ lệ tăng trưởng của số tiền là
growth_rate=(amount_after_10_years-amount_after_5_years)/amount_after_5_years
print("Số tiền sau 5 năm là:",round(amount_after_5_years, 2))
print("Số tiền sau 10 năm là:",round(amount_after_10_years, 2))
print("Tỉ lệ tăng trưởng là:",round(growth_rate, 2),"%")

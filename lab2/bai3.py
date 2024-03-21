# nhập vào một số nguyên có ba chữ số. in ra cách đọc của số nguyên này theo tiếng anh
so=int(input("nhập vào số nguyên : "))
chu_so_hang_tram = so // 100
chu_so_hang_chuc = ( so //10) % 10
chu_so_hang_don_vi = so % 10
if chu_so_hang_tram == 1:
        hang_tram = "one hundred"
elif chu_so_hang_tram == 2:
        hang_tram = "two hundred"
elif chu_so_hang_tram == 3:
        hang_tram = "three hundred"
elif chu_so_hang_tram == 4:
        hang_tram = "four hundred"
elif chu_so_hang_tram == 5:
        hang_tram = "five hundred"
elif chu_so_hang_tram == 6:
        hang_tram = "six hundred"
elif chu_so_hang_tram == 7:
        hang_tram = "seven hundred"
elif chu_so_hang_tram == 8:
        hang_tram = "eight hundred"
elif chu_so_hang_tram == 9:
        hang_tram = "nine hundred"
elif chu_so_hang_tram == 0:
        hang_tram = "" 
if chu_so_hang_chuc == 1:
        if chu_so_hang_don_vi == 0:
            hang_chuc = "ten"
        elif chu_so_hang_don_vi == 1:
            hang_chuc = "eleven"
        elif chu_so_hang_don_vi == 2:
            hang_chuc = "twelve"
        elif chu_so_hang_don_vi == 3:
            hang_chuc = "thirteen"
        elif chu_so_hang_don_vi == 4:
            hang_chuc = "fourteen"
        elif chu_so_hang_don_vi == 5:
            hang_chuc = "fifteen"
        elif chu_so_hang_don_vi == 6:
            hang_chuc = "sixteen"
        elif chu_so_hang_don_vi == 7:
            hang_chuc = "seventeen"
        elif chu_so_hang_don_vi == 8:
            hang_chuc = "eighteen"
        elif chu_so_hang_don_vi == 9:
            hang_chuc = "nineteen"
        so_hang_don_vi = ""
else:
        if chu_so_hang_chuc == 2:
            hang_chuc = "twenty"
        elif chu_so_hang_chuc == 3:
            hang_chuc = "thirty"
        elif chu_so_hang_chuc == 4:
            hang_chuc = "forty"
        elif chu_so_hang_chuc == 5:
            hang_chuc = "fifty"
        elif chu_so_hang_chuc == 6:
            hang_chuc = "sixty"
        elif chu_so_hang_chuc == 7:
            hang_chuc = "seventy"
        elif chu_so_hang_chuc == 8:
            hang_chuc = "eighty"
        elif chu_so_hang_chuc == 9:
            hang_chuc = "ninety"
        elif chu_so_hang_chuc == 0:
            hang_chuc = ""
if chu_so_hang_don_vi != 0 and chu_so_hang_chuc != 1:
        if chu_so_hang_don_vi == 1:
            hang_don_vi= "one"
        elif chu_so_hang_don_vi == 2:
            hang_don_vi = "two"
        elif chu_so_hang_don_vi == 3:
            hang_don_vi = "three"
        elif chu_so_hang_don_vi == 4:
            hang_don_vi = "four"
        elif chu_so_hang_don_vi == 5:
            hang_don_vi = "five"
        elif chu_so_hang_don_vi == 6:
            hang_don_vi = "six"
        elif chu_so_hang_don_vi == 7:
            hang_don_vi = "seven"
        elif chu_so_hang_don_vi == 8:
            hang_don_vi = "eight"
        elif chu_so_hang_don_vi == 9:
            hang_don_vi = "nine"
        elif chu_so_hang_don_vi == 0:
            hang_don_vi = ""
print("số ", so ," đọc là: ", hang_tram , hang_chuc , hang_don_vi)
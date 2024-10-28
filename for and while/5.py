jumlah = 0
for a in range(1,6):
     print(a, end=" ") # + nya bermasalah di angka 5 nya ada + an
     jumlah += a # jumlah = jumlah + a
     if a < 5:
          print(end="+ ")
print("=", jumlah)
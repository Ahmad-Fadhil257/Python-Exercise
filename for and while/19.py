jumlah = []
total = 0
rata2 = 0

inputan = int(input("Masukkan jumlah yang ingin di input : "))

for a in range(inputan):
     jumlah.append(int(input("Masukkan inputan nilai : ")))

for akhir in jumlah:
     total += akhir
     rata2 = total / inputan
print ("Total nilai adalah : ",total)
print ("rata-rata nilai adalah : ",rata2)
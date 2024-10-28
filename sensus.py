sensus = []

penduduk = int(input("Masukkan jumlah penduduk : "))

for i in range(penduduk):
     sensus.append(float(input(f"Masukkan usia penduduk ke-{i+1} : ")))

total = 0
max1 = max2 = 0
min1 = min2 = 1000 # mengkondisikan, 1000 karna umur ga mungkin lebih dari 1000

for jumlah in sensus:
     total += jumlah

     if jumlah > max1:
         max2 = max1
         max1 = jumlah
     elif jumlah > max2:
          max2 = jumlah

     if jumlah < min1:
          min2 = min1
          min1 = jumlah
     elif jumlah < min2:
          min2 = jumlah
rata_rata = jumlah / penduduk

# print(f'\nRata-Rata umur nya adalah \t: {rata_rata} Tahun')
# print(f'Umur tertua 1 adalah  \t\t: {max1} Tahun')
# print(f'Umur tertua 2 adalah  \t\t: {max2} Tahun\n')

# print(f'Umur termuda 1 adalah \t\t: {min1} Tahun')
# print(f'Umur termuda 2 adalah \t\t: {min2} Tahun')

print(f'''
Rata-Rata umur nya adalah     : {rata_rata} Tahun
Umur tertua 1 adalah          : {max1} Tahun
Umur tertua 2 adalah          : {max2} Tahun 

Umur termuda 1 adalah         : {min1} Tahun
Umur termuda 2 adalah         : {min2} Tahun
     ''')
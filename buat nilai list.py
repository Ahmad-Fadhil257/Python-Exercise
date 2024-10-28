nilai = [ ]

inputan = int(input("Masukkan jumlah inputan: "))

for i in range(inputan):
     nilai.append(float(input(f'Nilai ke-{i+1} : ')))

total = max = 0
min = nilai[0]

for data in nilai:
     total += data #"+=" adalah total = total + data
     if data > max:
          max = data

     if data < min:
          min = data

rata_rata = total / inputan

print(f"Nilai Terbesar  : {max}")
print(f"Nilai Terkecil  : {min}")
print(f"Nilai Rata-Rata : {rata_rata}")
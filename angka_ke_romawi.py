angka = int(input('Masukkan angka 1-10 \t: '))

romawi = ['I', 'II', 'III','IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

if 1 <=  angka <= 10:
 print(f"{angka} dalam angka romawi adalah : {romawi[angka-11]}")
else:
 print("masukkan salah")
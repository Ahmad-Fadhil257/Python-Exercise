# Program menghitung luas dan keliling belah ketupat
diagonal1 = float(input("Masukkan diagonal pertama belah ketupat: "))
diagonal2 = float(input("Masukkan diagonal kedua belah ketupat: "))
sisi = float(input("Masukkan panjang sisi belah ketupat: "))

luas = (diagonal1 * diagonal2) / 2
keliling = 4 * sisi

print(f"Luas belah ketupat: {luas}")
print(f"Keliling belah ketupat: {keliling}")

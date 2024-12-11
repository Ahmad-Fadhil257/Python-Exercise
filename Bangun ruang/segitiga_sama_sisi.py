# Program menghitung luas dan keliling segitiga sama sisi
sisi = float(input("Masukkan panjang sisi segitiga sama sisi: "))


luas = (sisi ** 2 * (3 ** 0.5)) / 4
keliling = 3 * sisi

print(f"Luas segitiga sama sisi: {luas}")
print(f"Keliling segitiga sama sisi: {keliling}")

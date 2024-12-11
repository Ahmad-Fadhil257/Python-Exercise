# Program menghitung luas dan keliling segitiga sama kaki
alas = float(input("Masukkan panjang alas segitiga sama kaki: "))
tinggi = float(input("Masukkan tinggi segitiga sama kaki: "))
sisi_miring = float(input("Masukkan panjang sisi miring segitiga sama kaki: "))


luas = (alas * tinggi) / 2
keliling = alas + 2 * sisi_miring

print(f"Luas segitiga sama kaki: {luas}")
print(f"Keliling segitiga sama kaki: {keliling}")

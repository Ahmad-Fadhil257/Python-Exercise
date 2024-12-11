# Program menghitung luas dan keliling trapesium
a = float(input("Masukkan panjang sisi atas trapesium: "))
b = float(input("Masukkan panjang sisi bawah trapesium: "))
tinggi = float(input("Masukkan tinggi trapesium: "))
sisi_miring = float(input("Masukkan panjang sisi miring trapesium: "))


luas = ((a + b) * tinggi) / 2
keliling = a + b + 2 * sisi_miring

print(f"Luas trapesium: {luas}")
print(f"Keliling trapesium: {keliling}")

# Program menghitung luas dan keliling trapesium sama kaki
sisi_atas = float(input("Masukkan panjang sisi atas: "))
sisi_bawah = float(input("Masukkan panjang sisi bawah: "))
tinggi = float(input("Masukkan tinggi trapesium: "))
sisi_miring = float(input("Masukkan panjang sisi miring: "))


luas = ((sisi_atas + sisi_bawah) * tinggi) / 2
keliling = sisi_atas + sisi_bawah + 2 * sisi_miring

print(f"Luas trapesium sama kaki: {luas}")
print(f"Keliling trapesium sama kaki: {keliling}")

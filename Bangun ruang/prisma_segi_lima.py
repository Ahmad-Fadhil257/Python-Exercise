# Program menghitung volume prisma segi lima
sisi = float(input("Masukkan panjang sisi segi lima: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))


luas_alas = (5 / 2) * sisi * (sisi / (2 * (3.14 / 5)))
volume = luas_alas * tinggi_prisma

print(f"Volume prisma segi lima: {volume}")

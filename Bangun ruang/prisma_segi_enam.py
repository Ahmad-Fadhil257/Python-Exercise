# Program menghitung volume dan luas permukaan prisma segi enam
sisi = float(input("Masukkan panjang sisi segi enam: "))
tinggi_prisma = float(input("Masukkan tinggi prisma segi enam: "))


luas_alas = (3 * (sisi ** 2) * (3 ** 0.5)) / 2
volume = luas_alas * tinggi_prisma
luas_permukaan = 2 * luas_alas + 6 * sisi * tinggi_prisma

print(f"Volume prisma segi enam: {volume}")
print(f"Luas permukaan prisma segi enam: {luas_permukaan}")

# Program menghitung volume dan luas permukaan prisma segitiga
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))

luas_alas = (alas * tinggi_segitiga) / 2
volume = luas_alas * tinggi_prisma
luas_permukaan = (2 * luas_alas) + (3 * alas * tinggi_prisma)

print(f"Volume prisma segitiga: {volume}")
print(f"Luas permukaan prisma segitiga: {luas_permukaan}")

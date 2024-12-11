# Program menghitung volume prisma hexagonal
sisi = float(input("Masukkan panjang sisi hexagonal: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))


luas_alas = (3 * 3.14 * (sisi ** 2)) / 4
volume = luas_alas * tinggi_prisma

print(f"Volume prisma hexagonal: {volume}")

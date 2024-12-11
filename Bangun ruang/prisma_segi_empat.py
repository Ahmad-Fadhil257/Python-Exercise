# Program menghitung volume dan luas permukaan prisma segi empat
panjang = float(input("Masukkan panjang alas: "))
lebar = float(input("Masukkan lebar alas: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))


luas_alas = panjang * lebar
volume = luas_alas * tinggi_prisma
luas_permukaan = 2 * luas_alas + 2 * (panjang + lebar) * tinggi_prisma

print(f"Volume prisma segi empat: {volume}")
print(f"Luas permukaan prisma segi empat: {luas_permukaan}")

# Program menghitung volume limas segi empat
panjang = float(input("Masukkan panjang alas: "))
lebar = float(input("Masukkan lebar alas: "))
tinggi = float(input("Masukkan tinggi limas: "))


luas_alas = panjang * lebar
volume = (1 / 3) * luas_alas * tinggi

print(f"Volume limas segi empat: {volume}")

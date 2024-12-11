# Program menghitung volume limas hexagonal
sisi = float(input("Masukkan panjang sisi hexagonal: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))


luas_alas = (3 * 3.14 * (sisi ** 2)) / 4
volume = (1 / 3) * luas_alas * tinggi_limas

print(f"Volume limas hexagonal: {volume}")

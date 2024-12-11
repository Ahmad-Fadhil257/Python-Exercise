# Program menghitung volume limas segi enam
sisi = float(input("Masukkan panjang sisi segi enam: "))
tinggi_limas = float(input("Masukkan tinggi limas segi enam: "))


luas_alas = (3 * (sisi ** 2) * (3 ** 0.5)) / 2
volume = (1 / 3) * luas_alas * tinggi_limas

print(f"Volume limas segi enam: {volume}")

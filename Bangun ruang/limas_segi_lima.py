# Program menghitung volume limas segi lima
sisi = float(input("Masukkan panjang sisi segi lima: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))


luas_alas = (5 / 2) * sisi * (sisi / (2 * (3.14 / 5)))
volume = (1 / 3) * luas_alas * tinggi_limas

print(f"Volume limas segi lima: {volume}")

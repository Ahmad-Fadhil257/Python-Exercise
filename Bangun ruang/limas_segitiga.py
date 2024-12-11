# Program menghitung volume dan luas permukaan limas segitiga
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi_alas = float(input("Masukkan tinggi alas segitiga: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))


luas_alas = (alas * tinggi_alas) / 2
volume = (1 / 3) * luas_alas * tinggi_limas

print(f"Volume limas segitiga: {volume}")

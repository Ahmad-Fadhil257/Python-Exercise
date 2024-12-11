# Program menghitung luas dan keliling segitiga siku-siku
alas = float(input("Masukkan panjang alas segitiga siku-siku: "))
tinggi = float(input("Masukkan tinggi segitiga siku-siku: "))


sisi_miring = (alas ** 2 + tinggi ** 2) ** 0.5
luas = (alas * tinggi) / 2
keliling = alas + tinggi + sisi_miring

print(f"Luas segitiga siku-siku: {luas}")
print(f"Keliling segitiga siku-siku: {keliling}")

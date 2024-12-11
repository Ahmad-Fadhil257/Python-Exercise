# Program menghitung luas trapesium tak beraturan
a = float(input("Masukkan panjang sisi sejajar pertama: "))
b = float(input("Masukkan panjang sisi sejajar kedua: "))
tinggi = float(input("Masukkan tinggi trapesium: "))


luas = ((a + b) * tinggi) / 2

print(f"Luas trapesium tak beraturan: {luas}")

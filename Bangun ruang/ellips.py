# Program menghitung luas dan keliling ellips
jari_jari_panjang = float(input("Masukkan jari-jari panjang ellips: "))
jari_jari_pendek = float(input("Masukkan jari-jari pendek ellips: "))


luas = 3.14 * jari_jari_panjang * jari_jari_pendek
keliling = 2 * 3.14 * ((jari_jari_panjang + jari_jari_pendek) / 2)

print(f"Luas ellips: {luas}")
print(f"Keliling ellips: {keliling}")

berat = float(input("Masukkkan jumlah berat (kg)\t\t: "))
kecepatan = float(input("Masukkan jumlah kecepatan (m/s)\t\t: "))
jari_jari = float(input("Masukkan jumlah jari jari (m)\t\t: "))

Sentripetal = berat * kecepatan**2 /jari_jari

print (f"Gaya sentripetal nya adalah : {Sentripetal} Newton")
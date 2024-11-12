berat = float(input("Masukkkan jumlah berat (kg)\t\t: "))
tinggi = float(input("Masukkkan jumlah tinggi (meter)\t\t: "))
gravitasi = float(input("Masukkkan jumlah gravitasi (m/s^2)\t: "))

Ep = berat * tinggi * gravitasi

print(f"Energi Potensial adalah : {Ep} joule")
print(f"Energi Potensial adalah : {Ep/1000} Kilo joule")
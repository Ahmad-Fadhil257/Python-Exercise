tegangan = float(input("Masukkkan jumlah tegangan (volt)\t\t: "))
kuat_arus = float(input("Masukkan jumlah kuat arus (Ampere)\t\t: "))

hambatan = tegangan / kuat_arus

print(f"Besar hambatan adalah : {hambatan} Ohm")    
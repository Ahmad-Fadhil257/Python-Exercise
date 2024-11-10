print("===============================")
print("Mengkonversi meter ke yang lain")
print("===============================")

yard = 0.9144
kaki = 0.3048
inchi = 0.0254
meter = float(input("Masukkan panjang benda dalam satuan meter : "))

yard = int(meter / yard)
kaki = int(meter / kaki)
inchi = int(meter / inchi)

print(f"{meter} meter = {yard} yard")
print(f"{meter} meter = {kaki} kaki")
print(f"{meter} meter = {inchi} inchi")

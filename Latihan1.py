Status_Lampu = input ("Status Lampu : ").lower()
Warna_Lampu = input ("Warna Lampu : ").lower()

if Status_Lampu == "menyala":
     if Warna_Lampu == "merah":
          print ("Berhenti")
     elif Warna_Lampu == 'kuning':
          print ("Bersiap")
     elif Warna_Lampu == 'hijau':
          print ("Maju")
else:
     print ("Terobos")

     #untuk biar ada jarak nya pencet tombol tab, biar jalan dan biar rapih
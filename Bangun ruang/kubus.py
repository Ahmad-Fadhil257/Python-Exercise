print("        VOLUME KUBUS         ")

def vkubus():
     Panjang = int(input("Masukkan Panjang (cm)  : "))
     tinggi = int(input("Masukkan Tinggi (cm)    : "))
     lebar = int(input("Masukkan Lebar (cm)      : "))

     Kubus = lambda p,t,l: p * t * l

     print (f"VOLUME KUBUS ADALAH: {Kubus(Panjang,tinggi,lebar)} cm ")
     print (f"VOLUME KUBUS ADALAH: {Kubus(Panjang,tinggi,lebar) / 100} m ")
vkubus()
vkubus()
vkubus()
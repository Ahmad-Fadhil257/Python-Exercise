print('MENGHITUNG VOLUME BOLA')

def bola():
     jari_jari = int(input("Masukkan ukuran jari jari (cm) : "))

     volume = lambda v : int(4/3 * 3.14 * v ** 3)
     
     print (f"Volume bola adalah : {volume(jari_jari)} cm")
     print (f"Volume bola adalah : {volume(jari_jari) / 100} m")

bola()
bola()
bola()
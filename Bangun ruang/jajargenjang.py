print ("============")
print ('Jajar genjang')
print ("------------")

def Jajar_genjang():
     alas = int(input('masukan nilai alas\t:'))

     tinggi = int(input('masukan nilai tinggi\t:'))

     sisi = int(input('Masukkan nilai sisi\t:'))

     luas = lambda a,t: alas * tinggi
     keliling = lambda s: 3 * sisi

     print('luas\t\t\t:',luas(alas,tinggi),'cm2')
     print ('keliling\t\t:',keliling(sisi),'cm2')
Jajar_genjang()
Jajar_genjang()
Jajar_genjang()

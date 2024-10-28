print('=============================')
print('\tSegitiga')
print('=============================')

def segitiga():
     Alas = int(input('Masukan nilai Alas\t: '))
     Tinggi = int(input('Masukan nilai Tinggi\t: '))

     Luas = lambda a,b: 1/2 * Alas * Tinggi

     print(f'Luas\t\t:{Luas(Alas,Tinggi)}cm2')

     Sisi = int(input('Masukan nilai Sisi\t: '))

     Keliling = lambda c: 3 * Sisi
     print(f'Keliling\t\t:{Keliling(Sisi)}cm2')
     
segitiga()
segitiga()
segitiga()
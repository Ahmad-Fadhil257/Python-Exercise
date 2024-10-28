print('==================================')
print('MENCARI LUAS DAN KELILING PERSEGI')
print('==================================')

def persegi():
     sisi = int(input('Masukan nilai sisi\t: '))

     Luas = lambda a: sisi * sisi

     Keliling = lambda a: 4 * sisi

     print(f'Luas persegi\t\t:{Luas(sisi)}cm2')
     print(f'Keliling persegi\t:{Keliling(sisi)}cm2')

persegi()
persegi()
persegi()
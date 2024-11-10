print('==================================')
print('MENCARI LUAS DAN KELILING PERSEGI PANJANG')
print('==================================')

def persegi_panjang():
     pj = int(input('Masukan nilai panjang\t: '))
     lb = int(input('Masukkan nilai lebar \t:'))

     luas = lambda a,b: pj * lb

     Keliling = lambda a,b: 2 * pj * lb

     print(f'Luas persegi panjang\t\t: {luas(pj,lb)} cm2')
     print(f'Keliling persegi panjang\t: {Keliling(pj,lb)} cm2')
persegi_panjang()
persegi_panjang()
persegi_panjang()
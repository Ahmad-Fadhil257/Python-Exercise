print('=========================')
print('\tKerucut')
print('=========================')

jr2 = int(input('masukan nilai jari-jari\t:'))
t = int(input('Masukkan nilai tinggi\t:'))

volume = 3.14 * jr2 * jr2 * t

lp = 3.14 * jr2 * jr2

print('volume\t\t:',volume,'cm2')
print('volume\t:',volume / 10, 'm2')

tanya = str(input('apakah ingin mencari luas permukaan? [y/t] : '))
if tanya == 'y' :
    stry = int(input('Masukkan nilai sisi\t:'))

    lp2 = 3.14 * jr2 * stry
    
    print('luas permukaan\t\t:',lp2 + lp,'cm2')
    print('TERIMA KASIH')
elif tanya == 't' :
    print('OK terima Kasih')

else:
    print('pilihan tidak ada')
print('=========================')
print('\tLingkaran')
print('=========================')

jr2 = int(input('masukan nilai jari-jari\t:'))

luas = 22/7 * jr2 * jr2
keliling = 2 * 22/7 * jr2
print('luas\t\t:',luas,'cm2')

tanya = str(input('apakah ingin mencari keliling [y/t] : '))
if tanya == 'y' :
    print('kelilingt\t\t:',keliling,'cm2')
    print('TERIMA KASIH')
elif tanya == 't' :
    print('OK terima Kasih')
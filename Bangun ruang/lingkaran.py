print('=========================')
print('\tLingkaran')
print('=========================')

def lingkaran():
    jr2 = int(input('masukan nilai jari-jari\t:'))

    luas = lambda a: 22/7 * jr2 * jr2

    keliling = lambda a: 2 * 22/7 * jr2

    print(f'luas\t\t: {int(luas(jr2))} cm2')

    tanya = str(input('apakah ingin mencari keliling [y/t] : '))
    if tanya == 'y' :
        print(f'keliling\t\t: {int(keliling(jr2))} cm2')
        print('TERIMA KASIH')

    elif tanya == 't' :
        print('OK Terima Kasih')

lingkaran()
lingkaran()
lingkaran()
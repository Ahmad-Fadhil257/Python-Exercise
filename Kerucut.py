print('=========================')
print('\tKerucut')
print('=========================')

def kerucut():
    jari2 = int(input('masukan nilai jari-jari\t:'))
    tinggi = int(input('Masukkan nilai tinggi\t:'))
    sisi = int(input('Masukkan nilai sisi\t:'))

    volume = lambda jr2,t: int(3.14 * jr2 * jr2 * t)
    lp2 = lambda jr2,s: int(3.14 * jr2 * s)
    lp = lambda jr2: int(3.14 * jr2 * jr2)

    print(f'volume\t\t: {volume(jari2,tinggi)} cm2')
    print(f'volume\t\t: {int(volume(jari2,tinggi) / 10)} m2')
    print(f'luas permukaan\t: {lp2(jari2,sisi) + lp(jari2)} cm2')

kerucut()
kerucut()
kerucut()
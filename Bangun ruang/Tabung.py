print ("============")
print ('   Tabung   ')
print ("------------")

def tabung():
     r = int(input('masukan nilai jari-jari\t: '))
     tinggi = int(input('masukan nilai tinggi\t: '))

     volume = lambda a,b: 3.14 * r * r * tinggi
     lp = lambda : 2 * 3.14 
     aa = lambda a,b: r + tinggi

     print(f'Volume\t\t\t: {int(volume (r,tinggi) )} cm2')
     print(f'Luas Permukaan\t\t: {int(aa (r,tinggi) * lp () )} cm2')

tabung()
tabung()
tabung()
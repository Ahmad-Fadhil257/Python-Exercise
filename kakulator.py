print('======================')
print('Kalkulator sederhana')
print('======================')

a1 = int(input('Masukkan nomer pertama \t: '))
option = input('pilih opsi( + - * /) \t: ')
a2 = int(input('Masukkan nomer kedua\t: '))

opsiplush = a1 + a2
opsimin = a1 - a2
opsikali = a1 * a2
opsibagi = a1 / a2

if option == '+':
    print('Hasilnya :\t' + str(opsiplush))

elif option == '-':
    print('Hasilnya :\t' + str(opsimin))

elif option == '*':
    print('Hasilnya :\t' + str(opsikali))

elif option == '/':
    print('Hasilnya :\t' + str(opsibagi))

else:
    print('ERROR silahkan coba lagi')

print('TERIMA KASIH')
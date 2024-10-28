print('======================')
print('Kalkulator sederhana')
print('======================')

operand1 = int(input('Masukkan nomer pertama \t: '))
operator = input('pilih opsi( + - * /) \t: ')
operand2 = int(input('Masukkan nomer kedua\t: '))

opsiplush = operand1 + operand2
opsimin = operand1 - operand2
opsikali = operand1 * operand2
opsibagi = operand1 / operand2

if operator == '+':
    print ('Hasilnya :\t' + str(opsiplush))

elif operator == '-':
    print('Hasilnya :\t' + str(opsimin))

elif operator == '*':
    print('Hasilnya :\t' + str(opsikali))

elif operator == '/':
    print('Hasilnya :\t' + str(opsibagi))

else:
    print('ERROR silahkan coba lagi')

print('\tTERIMA KASIH')
a = input('введите ваше число ')
q = 0
w = 1
for i in a:
    q += int(i)
    w *= int(i)
print (f'сумма {q}')
print (f'произведение   {w}')

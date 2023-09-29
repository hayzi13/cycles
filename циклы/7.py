a = int(input('введите ваше число '))
q = 0
if  a > 0:
        for i in str(a):
            if int(i) % 2 == 0:
                q += int(i)
        print(f" сумму четных цифр {q}")

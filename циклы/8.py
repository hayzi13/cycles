q = []
a = int(input('a: '))

if a < 0:
        print('ошибка')
else:
    while a != 0:
        q.append(a % 10)
        a = a // 10
q.reverse()
w = 0
e = 1

for i in q:
     w += i
     e *= i
print(w, e)

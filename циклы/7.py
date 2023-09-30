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
for i in q:
    if i % 2 == 0:
        w += i
print(w)

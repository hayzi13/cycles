a = int(input('введите число '))
q = []
while a != 0:
    q.append(a % 10)
    a = a // 10
q.reverse()
print(q)

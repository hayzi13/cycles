a = int(input('введите значение  '))
q = [0, 1]
for i in range(1, a+1):
    if a <= 1:
        break
    q.append(q[i-1]+q[i])
if a > 1:
    q.pop(-1)
print(q)

a = int(input('введите число '))
b = int(input('введите степень '))
q = 1

if b > 0:
    for i in range(1, b+1):
        
        q*=a
print(q)

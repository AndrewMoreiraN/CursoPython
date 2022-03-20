t1 = (1, 2, 'andrew', 3, 'a') * 2
t2 = 1, 2, 3, 'a', 'moreira'
t3 = 1,
t4 = t1 + t2

n1, n2, n3, *_, n10 = t4
print('T1')
for i in t1:
    print(i)

print('T2')
print(t2[2:0:-1])

print('T3')
print(type(t3))

print('T4')
print(t4)

print(n10)

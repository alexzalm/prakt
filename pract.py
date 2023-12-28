import random
k = 0
n = random.randint(1, 10)
m = random.randint(1, 10)
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(random.randint(1, 100))
if n <= 2 or m <= 2:
    print('нет локальных минимумов')
    exit()
for i in a:
    for j in i:
        print(j, end=' ')
    print('\n')
for i in range(1, n-1):
    for j in range(1, m-1):
        pr = True
        if a[i+1][j] < a[i][j] or a[i-1][j] < a[i][j] or a[i][j+1] < a[i][j] or a[i][j-1] < a[i][j]:
            pr = False
        if pr:
            k += 1
print('в матрице', k, 'локальных минимумов')

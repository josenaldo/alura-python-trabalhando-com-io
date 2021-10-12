a = [1,2,3,4,5,6,7,8,9,10]

a10 = []

for elemento in a:
    multiplicado = elemento * 10
    a10.append(multiplicado)

print(a10)

a20 = [x * 20 for x in a if x % 2 == 0]
print(a20)
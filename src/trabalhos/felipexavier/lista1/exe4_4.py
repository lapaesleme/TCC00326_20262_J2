def maior (a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

num = input("Digite três números para ver qual é maior: ").split()
a = int(num[0])
b = int(num[1])
c = int(num[2])

print(f"O maior é {maior(a,b,c)}")

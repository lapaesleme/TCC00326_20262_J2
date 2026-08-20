def maior(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
num1 = int(input("digite um numero:"))
num2 = int(input("digite um numero:"))
num3 = int(input("digite um numero:"))

maiorNumero = maior(num1,num2,num3)
print("o maior numero é: ",maiorNumero)
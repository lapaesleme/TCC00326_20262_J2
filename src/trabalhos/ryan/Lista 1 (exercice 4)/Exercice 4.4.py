def numero (k,l,m):
   if k >= l:
       return k
   elif l >= m:
       return l
   else:
       return m

x = int(input("Digite a primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

numero_maior = (z)
print("O maior número é : ", numero_maior)
print()
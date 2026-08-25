notas = [0,7,2,3,48,8,5,-3,6,7,-2,8,9,10]
i = 0
for nota in notas:
    i = notas + i
    media = i / 11
print("media:", media)
if media > 7:
    print("bom")
elif media >= 5:
    print("ok")
else:
    print("baixo")
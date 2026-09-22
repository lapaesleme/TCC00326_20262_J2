

var = {"nome": "Luiz"}
#var = dict()

var["tel"]=99999999
var["nome"]="Andre"

print(list(var.items()))

for par in list(var.items()):
    print(par)

for chave, valor in list(var.items()):
    print(chave, valor)




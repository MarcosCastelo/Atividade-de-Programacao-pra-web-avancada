def mostra_dados(a,b,c):
    a = "nome: %s" % a
    b = "endereço: %s " % b
    c = "telefone: %s " % c

    return a,b,c
a = input("Digite o nome: ")
b = input("Digite o endereço: ")
c = input("Digite o telefone: ")

print(mostra_dados(a,b,c))

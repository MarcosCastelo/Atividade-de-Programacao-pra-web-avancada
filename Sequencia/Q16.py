a = float(input("Digite o valor da compra: "))
b = float(input("Digite o valor do tempo: "))
c = float(input("Digite o valor da taxa: "))

prestacao = a +(a *(c/100)*b)

print("Valor da prestação é: ", prestacao)

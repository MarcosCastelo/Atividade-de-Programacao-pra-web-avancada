ano = int(input("Digite o ano de nascimento: "))

def calcula_ano(n):
    return 2013 % n

print("Sua idade é: ",calcula_ano(ano))

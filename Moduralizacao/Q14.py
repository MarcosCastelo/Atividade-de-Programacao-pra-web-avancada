n = int(input("Digite um numero de 3 digitos: "))

def dezenas(n):
    return (n % 100) // 10

print("A casa das dezenas é: ", dezenas(n))


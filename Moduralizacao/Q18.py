a = int(input("Digite um numero inteiro: "))
b = int(input("Digite um numero inteiro: "))

def troca(a,b):
    a = a + b
    b = a - b
    a = a - b

    return a,b
print("Os valores de a e b são respectivamente invertidos:", troca(a,b))

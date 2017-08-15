def inverse(n):
    v = (n % 10) * 100 + ((n % 100)// 10) * 10 + (n // 100)
    return v

a = int(input("Digite um numero de 3 digitos: "))
print("O inverso do numero é: ", inverse(a))
    
    

q = float(input("Digite o valor do produto: "))
p = float(input("Digite o valor do percentual de desconto: "))

def desconto(q,p):
    return q-(q*(p/100))

print("O produto com desconto é ",desconto(q,p))

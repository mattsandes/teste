#Script para calcular o desconto de algum produto

valor_original = float(input('Digite o valor do produto: '))

valor_descontado = valor_original * 0.3

valor_final = valor_original * 0.70

print(f'Valor do produto é {valor_original}')
print(f'O valor do desconto é de {valor_descontado}')
print(f'Você vai pagar apenas {valor_final}')
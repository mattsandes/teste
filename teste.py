nota1 = float(input(''))
nota2 = float(input(''))

media = nota1 + nota2 / 2

print(f'Sua media é de {media}')

if media < 7.0:
    print('Reprovado')
else:
    print('Aprovado'
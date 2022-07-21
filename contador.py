sal = float(input('Informe seu salario atual: '))

if sal <= 280:
    print(f'Seu salario atual é de {sal}')
    print('Seu Salario foi ajustado em 20%')
    ajuste = sal * 0.2
    print(f'O valor do ajuste foi de {ajuste}')
    n_sal = ajuste + sal
    print(f'Seu novo salario é de {n_sal}')
elif sal >= 280 or sal <= 700:
    print(f'Seu salario atual é de {sal}')
    print('Seu Salario foi ajustado em 15%')
    ajuste = sal * 0.15
    print(f'O valor do ajuste no seu salario foi de R${ajuste}')
    n_sal = (ajuste + sal)
    print(f'Seu novo salario é de R${n_sal}')
elif sal >= 700 or sal <= 1500:
    print(f'Seu salario atual é de {sal}')
    print('Seu Salario foi ajustado em 10%')
    ajuste = sal * 0.1
    print(f'O valor do seu salario foi de R${ajuste}')
    n_sal = ajuste + sal
    print(f'Seu salario novo salario é de R${n_sal}')
elif sal >= 1500:
    print(f'Seu salario atual é de {sal}')
    print('Seu salario foi ajustado em 5%')
    ajuste = sal * 0.05
    print(f'O valor do seu salario foi de R${ajuste}')
    n_sal = ajuste + sal
    print(f'Seu salario novo salario é de R${n_sal}')
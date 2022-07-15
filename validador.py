#Válidando o nome do usuário

nome = input('Informe seu nome: ') 

if len(nome) < 3:
    print('Nome de usuario invalido')
    while len(nome) < 3:
        nome = input('Insira um usuario valido: ')
        if len(nome) > 3:
            break
    print('Usuario valido')
else:
    pass

# validando a idade

idade = int(input('Informe sua idade: '))

if idade < 0 or idade > 150:
    print('Idade invalida')
    while idade < 0 or idade > 150:
        idade = int(input('Informe uma idade valida: '))
        if idade > 0 or idade <= 150:
            break
else:
    pass

#validando salario

sal = float(input('Informe seu salario: '))

if sal < 0:
    print('Deixe de frescura')
    while sal < 0:
        sal = float(input('Diga logo: '))
        if sal > 0:
            print(sal)
else:
    pass

#validando sexo

sexo = input('Informe seu sexo: ')

if sexo == 'F' or sexo == 'f':
    pass
elif sexo == 'M' or sexo == 'm':
    pass
elif sexo != 'F' or sexo != 'f' or sexo != 'M' or sexo != 'm':
    print('Deixe de frescurx')
    while sexo != 'F' or sexo != 'f' or sexo != 'M' or sexo != 'm':
        sexo = input('É homi o muieh: ')
        if sexo == 'F' or sexo == 'f' or sexo == 'M' or sexo == 'm':
            break
else:
    pass

#validando estado civil

est_civil = input('Qual seu estado civil: ')

if est_civil == 'Solteiro' or est_civil == 'solteiro':
    pass
elif est_civil == 'Casado' or est_civil == 'casado':
    pass
elif est_civil == 'Divorciado' or est_civil == 'divorciado':
    print('Você é divorciado')
elif est_civil == 'Viúvo' or est_civil == 'viúvo':
    pass
elif est_civil != 'Solteiro' or est_civil != 'solteiro' or est_civil != 'Divorciado' or est_civil != 'divorciado' or est_civil != 'Viúvo' or est_civil != 'viúvo':
    pass
    while est_civil != 'Solteiro' or est_civil != 'solteiro' or est_civil != 'Divorciado' or est_civil != 'divorciado' or est_civil != 'Viúvo' or est_civil != 'viúvo':
        est_civil = input('Informe seu estado civil: ')
        if est_civil != 'Solteiro' or est_civil != 'solteiro' or est_civil != 'Divorciado' or est_civil != 'divorciado' or est_civil != 'Viúvo' or est_civil != 'viúvo':
            break
else:
    pass

print('\n')

#informações do usuario

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Sexo: {sexo}')
print(f'Estado Civil: {est_civil}')
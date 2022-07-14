dia = int(input('Informe o dia: '))
<<<<<<< HEAD
if dia > 31:
=======
    print('Dia invalido')
>>>>>>> teste2
    while dia > 31:
        dia = int(input('Insira um dia válido: '))
        if dia > 0 and dia <= 31:
            break

mes = int(input('Informe o mes: '))
if mes > 12:
    print('Mes invalido')
    while mes > 12:
        mes = int(input('Insira um mes valido: '))
        if mes > 0 and mes <= 12:
            break

ano = int(input('Informe o ano: '))

print(f'{dia}/{mes}/{ano}')
<<<<<<< HEAD
=======

>>>>>>> teste2

num= float(input('Um numero: '))
num2= float(input('Outro numero: '))
print("1- Soma")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")

opcao= int(input('Escolha uma opção: '))
if opcao == 1:
    resultado= num+num2
    print(f'A soma de {num} e {num2} é {resultado} ')
elif opcao == 2:
    resultado= num-num2
    print(f'A subtração de {num} e {num2} é {resultado}')
elif opcao == 3:
    resultado= num*num2
    print(f'A multiplicação de {num} e {num2} é {resultado}')
elif opcao == 4:
    if num2 != 0:
    resultado= num/num2
    else:
        print('ERRO: não é possivel fazer uma divisão por 0')
    print(f'A divisão de {num} e {num2} é {resultado}')
else:
    print('!!OPÇÃO INVALIDA!!')


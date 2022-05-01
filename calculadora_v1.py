# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print('Selecione o número da operação desejada:')
print('\n1 - Soma\n2 - Subtração\n3-Multiplicação\n4 - Divisão\n')
operacao = int(input('Digite sua opção (1/2/3/4):'))
num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))

def calculadora(op, n1, n2):
    if op == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif op == 2:
        print(f'{n1} - {n2} = {n1 - n2}')
    elif op == 3:
        print(f'{n1} * {n2} = {n1 * n2}')
    elif op == 4:
        print(f'{n1} / {n2} = {n1 / n2}')
    else:
        print('Opção inválida!')


calculadora(operacao, num1, num2)



'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''
print('SEQUÊNCIA DE FIBONACCI')
numeroAVerificar = int(input('Qual nº deseja ver se tem na Sequência de Fibonacci? '))
numero = 1
segNumero = 0

while True:
    tercNumero = numero + segNumero
    numero = segNumero
    segNumero = tercNumero
    
    if numeroAVerificar == tercNumero:
        print(f'O número {numeroAVerificar} pertece a Sequência de Fibonnaci!')
        break
    elif tercNumero > numeroAVerificar:
        print(f'O número {numeroAVerificar} NÃO pertece a Sequência de Fibonnaci!')
        break
print('\nFIM DO PROGRAMA')

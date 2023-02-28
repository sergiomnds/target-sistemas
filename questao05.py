'''
Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

frase = str(input('Informe a string a ser invertida: ')).upper().strip()

print(f'A frase {frase} fica assim quando invertida: ',end='')
for c in range(len(frase), 0, -1):
    print(f'{frase[c - 1]}', end='')
    
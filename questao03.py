'''
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''
import json
with open("dados.json") as dados:
    data = json.load(dados)
    
totalMensal = faturamentoSuperior = contador = 0

for c in data:
    numero = c['valor']
    contador += 1
    
    if numero > 0:
        totalMensal += c['valor']
    
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor and numero > 0:
            menor = numero

mediaMensal = totalMensal / 30

for c in data:
    if c['valor'] > mediaMensal:
        faturamentoSuperior += 1

print(f'''
DADOS DO FATURAMENTO
O menor valor de faturamento no mês (tirando dias sem faturamento) foi de R${menor:.2f}
O maior valor de faturamento no mês foi de R${maior:.2f}
A média do faturamento mensal foi de R${mediaMensal:.2f}
Desse modo, em {faturamentoSuperior} vezes no mês o faturamento diário foi superior à média mensal.
''')
    
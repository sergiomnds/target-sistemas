'''
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
'''
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros #180759.98
print('FATURAMENTO MENSAL DA DISTRIBUIDORA')
print(f'''
SP teve o faturamento mensal de R${sp}, representando {(sp / total)*100:.2f}% do valor total. 
RJ teve o faturamento mensal de R${rj}, representando {(rj / total)*100:.2f}% do valor total.
MG teve o faturamento mensal de R${mg}, representando {(mg / total)*100:.2f}% do valor total.
ES teve o faturamento mensal de R${es}, representando {(es / total)*100:.2f}% do valor total.
OUTROS teve o faturamento mensal de R${outros}, representando {(outros / total)*100:.2f}% do valor total.

Ao TOTAL foram R${total} faturados (100%).    
      ''')


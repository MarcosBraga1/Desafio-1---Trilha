'''
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
percentagem do distribuidor e dos impostos (aplicados, primeiro os impostos
sobre o custo de fábrica, e depois a percentagem do distribuidor sobre o resultado).
Supondo que a percentagem do distribuidor seja de 28% e os impostos 45%. Escrever
um algoritmo que leia o custo de fábrica de um carro e informe o custo ao consumidor
do mesmo. 
'''
def tributacao(valor):
  valor = valor + (valor * 0.45)
  valor = valor + (valor * 0.28)
  return valor

preco = float(input("Insira o valor de custo do veículo: "))
print(f"O preço de distribuição do mesmo é de: {tributacao(preco)}")
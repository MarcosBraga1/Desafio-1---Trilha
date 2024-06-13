'''
Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de
venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um
percentual informado pelo usuário.
'''
custo = float(input("Insira o valor de custo do produto: "))
percentil = float(input("Insira a porcentagem de acrescimo ao produto: "))
percentil = percentil / 100
print(f"O valor de venda do produto é de: {custo + (custo * percentil)}")
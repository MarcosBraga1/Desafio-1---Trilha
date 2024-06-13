'''
Faça um algoritmo para ler: a descrição do produto (nome), a quantidade
adquirida e o preço unitário.
Calcular e escrever o total (total = quantidade adquirida * preço unitário),
o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 
* Se quantidade <= 5 o desconto será de 2%
* Se quantidade > 5 e quantidade <=10 o desconto será de 3%
* Se quantidade > 10 o desconto será de 5%
'''
def calculo_valor():
  nome = input('Insira o nome do produto: ')
  quantidade = int(input('Insira a quantidade: '))
  valor = float(input('Insira o valor unitário: '))

  total = valor * quantidade
  print(f"O valor total do produto {nome} é: {total}")
  if quantidade <= 5:
    desconto = total * 0.02
    print(f"O valor do desconto é de {desconto} (2%), e o total: {total - desconto}")
  elif quantidade > 5 and quantidade <= 10:
    desconto = total * 0.03
    print(f"O valor do desconto é de {desconto} (3%), e o total: {total - desconto}")
  elif quantidade > 10:
    desconto = total * 0.05
    print(f"O valor do desconto é de {desconto} (5%), e o total: {total - desconto}")

calculo_valor()
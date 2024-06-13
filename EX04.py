'''
Crie um algoritmo que peça ao usuário que informe 10 números inteiros e
armazene-os em um vetor. A seguir, apresente a multiplicação de todos os
elementos pares e a soma de todos os elementos ímpares.
'''
def calculo(mult = 1, soma = 0):
  vetor = []
  for i in range(10):
    vetor.append(int(input(f"Insira o {i + 1} número inteiro: ")))

  print(vetor)

  for i in vetor:
    if i % 2 == 0:
      mult = mult * i
    else:
      soma = soma + i

  print(f"A multiplicação dos números inteiros é: {mult}")
  print(f"A soma dos números ímpares é: {soma}")

calculo()
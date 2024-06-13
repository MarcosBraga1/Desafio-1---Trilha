'''
Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando
“maior de idade” e “menor de idade” para cada pessoa. Considere a idade a partir
de 18 anos como maior de idade.
'''
contador = 0
while True:
  if contador == 75:
    break
  idade = int(input(f"Insira a idade da {contador + 1} pessoa: "))
  if idade <= 0:
    print("Idade inválida!")
  elif idade >= 18:
    print("Maior de idade.")
    contador += 1
  elif idade > 0 and idade < 18:
    print("Menor de idade.")
    contador += 1
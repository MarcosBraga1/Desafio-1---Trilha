'''
Desenvolva um algoritmo que leia uma string e determine se ela é um palíndromo.
Entrada: Uma string.
Saída: "É um palíndromo" ou "Não é um palíndromo".
'''
def palindromo():
  texto = input("Insira um texto para verificar se é um palíndromo: ")
  texto = ''.join(char.lower() for char in texto if char.isalnum())

  if texto == texto[::-1]:
    print("É um palíndromo")
  else:
    print("Não é um palíndromo")

palindromo()
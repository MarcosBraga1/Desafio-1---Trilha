'''
Desenvolva um algoritmo que conte quantas vogais existem em uma string fornecida pelo usuário.
Entrada: Uma string.
Saída: O número de vogais na string.
'''
contador = 0
texto = input("Insira um texto para contar as vogais: ").lower().strip()
vogais = ['a','e','i','o','u']

for i in texto:
  if i in vogais:
    contador += 1

print(f"O número de vogais no texto é de: {contador}.")
'''
Escreva um programa que leia uma lista de números e os ordene em ordem crescente.
Entrada: Uma lista de números.
Saída: A lista de números ordenada.
'''
lista = []
print("Insira números de forma aleatória. Digite 'fim' para sair.")

while True:
  entrada = input("Insira um número: ")
  if entrada == 'fim':
    break
  else:
    valor = int(entrada)
    lista.append(valor)
    
lista.sort()
print(lista)
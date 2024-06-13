'''
Desenvolva um algoritmo que calcule o fatorial de um número fornecido pelo usuário.
Entrada: Um número inteiro.
Saída: O fatorial desse número.
'''
def fatorial(num):
  if num < 0:
    return "Número inválido"
  elif num == 0 or num == 1:
    return 1
  else:
    return num * fatorial(num-1)
  
numero = int(input("Insira um número inteiro para calcular seu fatorial: "))
print(f"O fatorial de {numero} é: {fatorial(numero)}")
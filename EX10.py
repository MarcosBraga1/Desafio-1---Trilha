'''
Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de
forma que a variável A passe a possuir o valor da variável B e a variável B
passe a possuir o valor da variável A. Apresentar os valores trocados.
'''
def troca(a, b):
  aux = a
  a = b
  b = aux
  print(f"O valor de 'a' trocado é: {a}")
  print(f"O valor de 'b' trocado é: {b}")

a = input("Insira o valor de 'a': ")
b = input("Insira o valor de 'b': ")
troca(a, b)
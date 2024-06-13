'''
Aplicar um algoritmo que calcule a média das notas bimestrais de uma escola
(media = (nota1 + nota2 + nota3 + nota4)/4). O algoritmo deve repetir o cálculo
até que o usuário responda “N” à pergunta “Deseja continuar (S/N) ?”.
'''
def media():
  nota = []

  for i in range(4):
    n = float(input(f"Insira a {i + 1} nota: "))
    nota.append(n)
  
  media = sum(nota) / len(nota)
  print(f"A média é de: {media}")
  
media()

while True:
  res = input("Deseja continuar (S/N)?").lower()
  if res != "s" and res != "n":
    print("Resposta inválida!")
  elif res == "s":
    media()
  else:
    break
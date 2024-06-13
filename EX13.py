'''
Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno
durante o semestre. Calcular a sua média (aritmética), informar o nome e
sua menção aprovado (media maior ou igual 7), Reprovado (media <= 5) e
Recuperação (média entre 5.1 a 6.9).
'''
def media():
  nome = input("Insira o nome do aluno: ")
  nota = []

  for i in range(3):
    n = float(input(f"Insira a nota da {i + 1} prova: "))
    nota.append(n)

  media = sum(nota) / len(nota)
  
  print(f"Aluno: {nome}")
  if media <= 5:
    print("Aluno reprovado.")
  if media > 5 and media <= 6.9:
    print("Aluno de recuperação.")
  if media >= 7:
    print("Aluno aprovado.")

media()
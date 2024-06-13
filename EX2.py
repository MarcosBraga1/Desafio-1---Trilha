'''
Calcule quantos azulejos são necessários para azulejar uma parede.
É necessário conhecer a altura da parede (AP), a sua largura (LP), e a altura
do azulejo (A) e sua largura (LA). Leia os dados através do teclado.
'''
while True:
  AP = float(input('Insira a altura da parede (em metros): '))
  LP = float(input('Insira a largura da parede (em metros): '))
  A = float(input('Insira a altura do azulejo (em metros): '))
  LA = float(input('Insira a largura do azulejo (em metros): '))
  if all(valor > 0 for valor in [AP, LP, A, LA]):
    break
  else:
    print("Um dos valores inseridos é inválido!")

print(f"A quantidade de azulejos necessário para cobrir a parede são {(AP * LP)/(A * LA)}.")
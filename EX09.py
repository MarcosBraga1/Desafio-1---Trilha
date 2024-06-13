'''
Escreva um algoritmo para uma empresa que decide dar um reajuste a seus 584
funcionários de acordo com os seguintes critérios:
* 50% para aqueles que ganham menos do que 3 salários mínimos
* 20% para aqueles que ganham entre 3 a 10 salários mínimos
* 15% para aqueles que ganham de 10 a 20 salários mínimos
* 10% para os demais
'''
def reajuste(valor):
  salario = 1412
  if valor < (3 * salario):
    return valor + (valor * 0.5)
  elif valor >= (3 * salario) and valor < (10 * salario):
    return valor + (valor * 0.2)
  elif valor >= (10 * salario) and valor < (20 * salario):
    return valor + (valor * 0.15)
  elif valor >= (20 * salario):
    return valor + (valor * 0.1)
  
for i in range(584):
  salario = float(input("Insira o salario do funcionario para reajuste: "))
  print(f"O valor reajustado é de: {reajuste(salario)}")
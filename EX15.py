'''
A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos com
desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a
ser pago pelo cliente de vários carros. O desconto deverá ser calculado de acordo
com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema deverá
perguntar se deseja continuar calculando desconto até que a resposta seja: “(N) Não” .
Informar total de carros com ano até 2000 e total geral.
'''
def calculo():
  ano = int(input("Insira o ano do veículo: "))
  valor = float(input("Insira o seu custo: "))
  
  if ano <= 2000:
    valor = valor - (valor * 0.12)
  else:
    valor = valor - (valor * 0.07)

  print(f"O valor do veículo com desconto é de: {valor}")

calculo()

while True:
  res = input("Deseja continuar calculando? (S/N)").lower()
  if res != "s" and res != "n":
    print("Resposta inválida!")
  elif res == "s":
    calculo()
  else:
    break
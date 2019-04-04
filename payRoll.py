import os
def enterPayRoll():
  name = input("Nome:")
  salary = int(input("Salario: "))
  discount = int(input("Desconto: "))
  return name, salary, discount

def calc(salary,discount):
  sum = salary-discount
  return sum
  
def mainPayRoll():
  os.system("cls")
  print("{0:-^92}".format("Folha de Pagamento"))
  print()
  name, salary, discount = enterPayRoll()  
  result = calc(salary,discount)
  print("Usuario: {}".format(name))
  print("Salario Bruto: {}".format(salary))
  print("Desconto: {}".format(discount))
  print("Salario Liquido: {}".format(result))

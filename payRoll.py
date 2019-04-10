import os
import validate
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
  variables = [name, salary, discount, result]
  header = ["Usuario", "Salário Bruto", "Desconto", "Salario Liquido"]
  for i in range(len(variables)):
    print("`{}: {}".format(header[i],variables[i]))
  msgRepeat = "Deseja continuar calculando folha de pagamentos?[y/n] "
  validate.validateToRepeat(msgRepeat, lambda: mainPayRoll())


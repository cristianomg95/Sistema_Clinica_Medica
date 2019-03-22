from printAll import *
from register_remove import *
from graphcs import *
import os

def menu():
  os.system("cls")
  print("1 - Cadastrar Paciente")
  print("2 - Cadastrar Médico")
  print("3 - Marca Consulta")
  print("4 - Listar Pacientes")
  print("5 - Listar Médicos")
  print("6 - Remover Médico")
  print("7 - Listar Consultas")
  print("8 - Remover Consulta")
  print("9 - Folha de Pagamento dos Médicos")
  print("10 - Graficos de consultas por dia")
  print("11 - Graficos de consultas por mês")

  option = input("Escolha uma Opção: ")
  
  if option == "1":
    registerPatient()
  elif option == "2":
    registerDoctor()
  elif option == "3":
    registerQuery()
  elif option == "4":
    printPatients()
  elif option == "5":
    printDoctors()
  elif option == "6":
    removeDoctor()
  elif option == "7":
    printQuerys()
  elif option == "8":
    removeQuery()
  elif option == "9":
    printPayroll()
  elif option == "10":
    generateQueryGraphics('dia')
  elif option == "11":
    generateQueryGraphics('mes')

if __name__ == "__main__":
  menu()


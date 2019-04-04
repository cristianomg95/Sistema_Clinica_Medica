from load_Save import *
from validate import *
import os
from main import menu

def printHeader(parameters): # printar o cabeçalho // parameters é um vetor com todos os parametros
  for i in parameters:
    if i != "E-Mail":
      print("{0:<12}".format(i), end="")
    else:
      print("{0:<24}".format(i), end="")

def printHeader2(parameters): # printar o cabeçalho // parameters é um vetor com todos os parametros
  for i in parameters:
    print("{0:<20}".format(i), end="")


def printPayroll(): # listar folha de pagamentos
  pass

def printPatients(): # listar lista de pacientes
  os.system("cls")
  patients = loadPatients()
  parameters = ["Nome", "E-Mail", "Telefone", "RG", "CPF", "Endereço", "Numero", "Bairro", "Cidade", "Estado", "Plano de Saúde"]
  printHeader(parameters)
  print()
  for item in patients:
    for i in range(len(item)):
      if i != 1:
        print("{0:<12}".format(item[i]), end="")
      else:
        print("{0:<24}".format(item[i]), end="")
    print()
  msg = "Deseja voltar para o menu? [y/n]: "
  if validateToContinue(msg):
    menu()
  else:
    printPatients()

def printDoctors(): # listar lista de médicos
  os.system("cls")
  doctors = loadDoctors()
  parameters = ["Nome", "E-Mail", "Telefone", "Celular", "CRM", "RG", "CPF", "Especialização", "Endereço", "^Nº da Residencia", "Plano de Saúde"]
  printHeader(parameters)
  print()
  for item in doctors:
    for i in range(len(item)):
      if i != 1:
        print("{0:<12}".format(item[i]), end="")
      else:
        print("{0:<24}".format(item[i]), end="")
    print()
  msg = "Deseja voltar para o menu? [y/n]: "
  if validateToContinue(msg):
    menu()
  else:
    printDoctors()


def printQuerys(): # listar consultas
  os.system("cls")
  querys = loadQuerys()
  parameters = ["Nº da Consulta", "Nome do Médico", "Nome do Paciente", "Data", "Horário"]
  printHeader2(parameters)
  print()
  for item in querys:
    for i in item:
      print("{0:<20}".format(i), end="")
    print()
  msg = "Deseja voltar para o menu? [y/n]: "
  if validateToContinue(msg):
    menu()
  else:
    printQuerys()
    


  


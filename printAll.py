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


def printPatients(k): # listar lista de pacientes
  os.system("cls")
  patients = loadPatients()
  parameters = ["Nome", "E-Mail", "Telefone", "RG", "CPF", "Endereço", "Numero", "Bairro", "Cidade", "Estado", "Plano de Saúde"]
  printHeader(parameters)
  print()
  for item in patients[:5+k]:
    for i in range(len(item)):
      if i != 1:
        print("{0:<12}".format(item[i]), end="")
      else:
        print("{0:<24}".format(item[i]), end="")
    print()
  if len(patients[k:]) != 0:
    msg = "Deseja mostrar mais Pacientes? [y/n]: "
    if validateToContinue(msg):
      k = k+5
      printPatients(k)
    else:
      msg = "Deseja voltar para o menu? [y/n]: "
      if validateToContinue(msg):
        menu()
      else:
        printPatients(k)
  else:
    msg = "Deseja voltar para o menu? [y/n]: "
    if validateToContinue(msg):
      menu()
    else:
      printPatients(k)

def printDoctors(k): # listar lista de médicos
  os.system("cls")
  doctors = loadDoctors()
  parameters = ["Nome", "E-Mail", "Telefone", "Celular", "CRM", "RG", "CPF", "Espec", "End", "^Nº ", "Cidade", "UF", "Plano"]
  printHeader(parameters)
  print()
  for item in doctors[:5+k]:
    for i in range(len(item)):
      if i != 1:
        print("{0:<12}".format(item[i]), end="")
      else:
        print("{0:<24}".format(item[i]), end="")
    print()
  if len(doctors[k:]) != 0:
    msg = "Deseja mostrar mais Médicos? [y/n]: "
    if validateToContinue(msg):
      k = k+5
      printDoctors(k)
    else:
      msg = "Deseja voltar para o menu? [y/n]: "
      if validateToContinue(msg):
        menu()
      else:
        printDoctors(k)
  else:
    msg = "Deseja voltar para o menu? [y/n]: "
    if validateToContinue(msg):
      menu()
    else:
      printDoctors(k)


def printQuerys(k): # listar consultas
  os.system("cls")
  querys = loadQuerys()
  parameters = ["Nº da Consulta", "Nome do Médico", "Nome do Paciente", "Data", "Horário"]
  printHeader2(parameters)
  print()
  for item in querys[:5+k]:
    for i in item:
      print("{0:<20}".format(i), end="")
    print()
  if len(querys[k:]) != 0:
    msg = "Deseja mostrar mais Consultas? [y/n]: "
    if validateToContinue(msg):
      k = k+5
      printQuerys(k)
    else:
      msg = "Deseja voltar para o menu? [y/n]: "
      if validateToContinue(msg):
        menu()
      else:
        printQuerys(k)
  else:
    msg = "Deseja voltar para o menu? [y/n]: "
    if validateToContinue(msg):
      menu()
    else:
      printQuerys(k)


  


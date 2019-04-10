from load_Save import *
from time import sleep
from generateId import *
import os
import validate
import graphcs as gp


def registerPatient(): # cadastrar paciente
  os.system("cls")
  print("{0:-^92}".format("CADASTRO DE PACIENTES"))
  patient = []
  patients = loadPatients()
  variables = ["Nome", "E-Mail", "Telefone", "RG", "CPF", "Endereço", "Numero", "Bairro", "Cidade", "Estado", "Plano de Saúde"]
  for i in range(len(variables)):
    patient.append(input("{}: ".format(variables[i])))
  patients.append(patient)
  savePatient(patients)
  print("Cadastro realizado!!!")
  sleep(2)
  msg = "Deseja Cadastrar outro Paciente? [y/n]"
  validate.validateToRepeat(msg,lambda: registerPatient())

def registerDoctor(): # cadastrar médico
  os.system("cls")
  print("{0:-^92}".format("CADASTRO DE MÉDICOS"))
  doctors = loadDoctors()
  doctor = []
  variables = ["Nome", "E-Mail", "Telefone", "Celular", "CRM", "RG", "CPF", "Especialização", "End", "Nº da Residencia ", "Cidade", "UF", "Plano de Saude"]
  for i in range(len(variables)):
    doctor.append(input("{}: ".format(variables[i])))
  doctors.append(doctor)
  saveDoctor(doctors)
  print("Cadastro realizado!!!")
  sleep(2)
  msg = "Deseja Cadastrar outro Médico? [y/n]"
  validate.validateToRepeat(msg, lambda: registerDoctor())

def registerQuery(): # marcar consulta
  os.system("cls")
  querys = loadQuerys()
  ids = loadIds(querys)
  df = gp.loadDataFrame()
  query = []
  variables = ["Nome do Médico", "Nome do Paciente", "Data:(DD/MM/AAAA)", "Horário "]
  print("{0:-^92}".format("MARCAR CONSULTA"))
  query.append(generateId(ids))
  for i in range(len(variables)):
    query.append(input("{}: ".format(variables[i])))
  var = query[3].split("/")
  varD = (int(var[0])-1)
  varM = (int(var[1])-1)
  df[varM][varD] = df[varM][varD]+1
  gp.saveDataFrame(df)
  querys.append(query)
  saveQuery(querys)
  print("Consulta Marcarda!!!")
  sleep(2)

  msg = "Deseja continuar marcando consultas? [y/n]: "
  validate.validateToRepeat(msg, lambda: registerQuery())

def removeDoctor(): ## função para remover medicos do sistema
  os.system("cls")
  doctors = loadDoctors()
  print("{0:-^92}".format("REMOVER MÉDICOS"))
  name = input("Nome do Médico a ser removido: ").lower()
  msgRepeat = "Deseja Continuar Removendo?[y/n]: "
  findTrue = False
  doctorRecord = []
  for i in doctors:
    if name == i[0]:
      findTrue = True
      doctorRecord = i
  if findTrue:
    msgAccept = "Tem certeza que deseja remover o médico {} ?[y/n]: ".format(doctorRecord[0])
    if validate.validateToContinue(msgAccept):
      doctors.remove(doctorRecord)
      saveDoctor(doctors)
  else:
    print("Médico não encontrado!!")
  msgRepeat = "Deseja continuar removendo Médicos?[y/n] "
  validate.validateToRepeat(msgRepeat, lambda: removeDoctor())

def removeQuery():
  os.system("cls")
  querys = loadQuerys()
  print("{0:-^92}".format("REMOVER CONSULTA"))
  queryId = int(input("Numero da consulta: ")) 
  findTrue = False
  for query in querys:
    if query[0] == queryId:
      print(query)
      queryRecord = query
      findTrue = True

  if findTrue:
    msg = "Tem certeza que deseja remover a consulta [y/n]"
    if validate.validateToContinue(msg):
      querys.remove(queryRecord)
      var = queryRecord[3].split("/")
      varD = (int(var[0]) - 1)
      varM = (int(var[1]) - 1)
      df[varM][varD] = df[varM][varD] - 1
      gp.saveDataFrame(df)
      saveQuery(querys)
  else:
    print("Consulta não encontrada!!")
  msgRepeat = "Deseja continuar removendo consultas?[y/n] "
  validate.validateToRepeat(msgRepeat, lambda: removeQuery())
from load_Save import *
from time import sleep
from generateId import *
import os
import validate
import graphcs as gp

def registerPatient(): # cadastrar paciente
  os.system("cls")
  patient = []
  patients = loadPatients()
  print("{0:-^92}".format("CADASTRO DE PACIENTES"))

  name = input("Nome do paciente: ").lower()
  patient.append(name)
  email = input("E-mail: ").lower()
  patient.append(email)
  phone = input("Telefone: ").lower()
  patient.append(phone)
  rg = input("Registro Geral (RG): ").lower()
  patient.append(rg)
  cpf = input("CPF: ").lower()
  patient.append(cpf)

  print("{0:-^42}".format("ENDEREÇO"))

  address = input("Endereço:").lower()
  patient.append(address)
  number = input("Número da residência: ").lower()
  patient.append(number)
  neighborhood = input("Bairro: ").lower()
  patient.append(neighborhood)
  city = input("Cidade: ").lower()
  patient.append(city)
  uf = input("Estado: ").lower()
  patient.append(uf)
  healthPlan = input("Plano de Saúde: ").lower()
  patient.append(healthPlan)

  patients.append(patient)
  savePatient(patients)
  print("Cadastro realizado!!!")
  sleep(2)

  msg = "Deseja Cadastrar outro Paciente? [y/n]"
  validate.validateToRepeat(msg,lambda: registerPatient())

def registerDoctor(): # cadastrar médico
  os.system("cls ")
  doctors = loadDoctors()
  print("{0:-^92}".format("CADASTRO DE MÉDICOS"))
  doctor = []

  name = input("Nome: ").lower()
  doctor.append(name)
  email = input("E-mail: ").lower()
  doctor.append(email)
  phone = input("Telefone: ").lower()
  doctor.append(phone)
  cellPhone = input("Celular: ").lower()
  doctor.append(cellPhone)
  crm = input("CRM: ").lower()
  doctor.append(crm)
  rg = input("Registro Geral (RG): ").lower()
  doctor.append(rg)
  cpf = input("CPF: ").lower()
  doctor.append(cpf)
  specialization = input("ESpecialização: ").lower()
  doctor.append(specialization)

  print("{0:-^42}".format("ENDEREÇO"))

  street = input("Rua/Avenida: ").lower()
  doctor.append(street)
  number = input("Numero: ").lower()
  doctor.append(number)
  neighborhood = input("Bairro: ").lower()
  doctor.append(neighborhood)
  city = input("Cidade: ").lower()
  doctor.append(city)
  uf = input("UF: ").lower()
  doctor.append(uf)
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
  print("{0:-^92}".format("MARCAR CONSULTA"))
  query.append(generateId(ids))
  doctor = input("Nome do Médico: ")
  query.append(doctor)
  patient = input("Nome do Paciente: ")
  query.append(patient)
  date = input("Data:(DD/MM/AAAA")
  query.append(date)
  var = date.split("/")
  varD = int(var[0]-1)
  varM = int(var[1]-1)
  df[varM][varD] = df[varM][varD]+1
  gp.saveDataFrame(df)
  hour = input("Horário: ")
  query.append(hour)
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
    if validateToContinue(msgAccept):
      doctors.remove(doctorRecord)
      saveDoctor(doctors)
  else:
    print("Médico não encontrado!!")
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
      findTrue = True

  if findTrue:
    msg = "Tem certeza que deseja remover a consulta [y/n]"
    if validateToContinue(msg):
      querys.remove(query)
      saveQuery(querys)
  
  else:    
    print("Consulta não encontrada!!")
  msgRepet = "Deseja continuar removendo consultas?[y/n] "
  validate.validateToRepeat(msg, lambda: removeQuery())



  

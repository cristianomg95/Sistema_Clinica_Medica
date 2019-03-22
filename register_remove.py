from load_Save import *
from validate import *
import os
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

  msg = "Deseja Cadastrar outro Paciente? [y/n]"
  validateToRepeat(msg,lambda: registerPatient())

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

  msg = "Deseja Cadastrar outro Médico? [y/n]"
  validateToRepeat(msg, lambda: registerDoctor())

def registerQuery(): # marca consulta
  pass

def removeDoctor(): ## função para remover medicos do sistema
  os.system("cls")
  doctors = loadDoctors()
  print("{0:-^92}".format("REMOVER MÉDICOS"))
  name = input("Nome do Médico a ser removido: "),lower()
  msgRepeat = "Deseja Continuar Removendo?[y/n]: "
  findTrue = False
  doctorRecord = []
  for i in doctors:
    if name == i[0]:
      findTrue = True
      doctorRecord = i
  if findTrue:
    msgAccept = "Tem certeza que deseja remover o médico {} ?[y/n]: ".format(varAux2[0])
    if validateToContinue(msgAccept):
      doctors.remove(doctorRecord)
      saveDoctor(doctors)
  else:
    print("Médico não encontrado")
  validateToRepeat(msgRepeat, lambda: removeDoctor())



def removeQuery():
  pass
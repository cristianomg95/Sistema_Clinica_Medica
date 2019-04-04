import pickle as pk 

def loadPatients(): # carregar pacientes do banco de dados
  try:
    patients = pk.load(open("dados//patients.pickle", "rb"))
  except:
    print("criando arquivo de pacientes")
    patients = []
    pk.dump(patients, open("dados//patients.pickle", "wb") )  
  return patients

def loadDoctors(): # carregar médicos do banco de dados
  try:
    doctors = pk.load(open("dados//doctors.pickle", "rb"))
  except:
    print("criando arquivo de médicos")
    doctors = []
    pk.dump(doctors, open("dados//doctors.pickle", "wb") )
  return doctors 

def loadQuerys(): # carregar consultas do banco de dados
  try:
    querys = pk.load(open("dados//querys.pickle", "rb"))
  except:
    print("criando arquivo de consultas")
    querys = []
    pk.dump(querys, open("dados//querys.pickle", "wb") ) 
  return querys

def savePatient(patients): # salvar pacientes no banco de dados
  pk.dump(patients, open("dados//patients.pickle", "wb"))

def saveDoctor(doctors): # salvar médicos no banco de dados
  pk.dump(doctors, open("dados//doctors.pickle", "wb"))

def saveQuery(querys): # salvar consultas no banco de dados
  pk.dump(querys, open("dados//querys.pickle", "wb"))


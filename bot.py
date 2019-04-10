import load_Save as sv
import graphcs as gp
from random import randint
import generateId as gID
querys = sv.loadQuerys()
ids = gID.loadIds(querys)
df = gp.loadDataFrame()
for i in range(210):
    query = []
    rand = randint(1, 100)
    day = randint(1, 31)
    month = randint(1, 12)
    year = 2000
    h = randint(7, 18)
    m = randint(00, 59)
    doctor = 'medico{}'.format(rand)
    patient = 'paciente{}'.format(rand)
    date = "{}/{}/{}".format(day, month, year)
    hour = "{}:{}".format(h, m)
    variables = [doctor, patient, date, hour]
    query.append(gID.generateId(ids))
    for k in range(len(variables)):
        query.append("{}: ".format(variables[k]))
    var = date.split("/")
    varD = (int(var[0]) - 1)
    varM = (int(var[1]) - 1)
    df[varM][varD] = df[varM][varD] + 1
    gp.saveDataFrame(df)
    querys.append(query)
    sv.saveQuery(querys)


from random import randint

def generateId(ids):
  tempId = randint(10000,99999)
  if tempId in ids:
      generateID(ids)
  else:
    return tempId

def loadIds(querys):
  try:
    ids = []
    for query in querys:
      ids.append(query[0])
    return ids
  except:
    ids = []
    return ids
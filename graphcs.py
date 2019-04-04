import numpy as np
import pandas as pd
import pickle as pk
import matplotlib.pyplot as plt

def generateQueryGraphics():
  df = loadDataFrame()
  df = pd.DataFrame(df)
  plt.figure();
  df.boxplot()
  plt.show()
  


def loadDataFrame():
  try:
    df = pk.load(open("dados//dataframe.pickle", "rb"))
  except:
    print("criando arquivo de pacientes")
    df = np.zeros((12, 31), dtype=int)
    pk.dump(df, open("dados//dataframe.pickle", "wb") )  
  return df

def saveDataFrame(df):
  pk.dump(df, open("dados//dataframe.pickle", "wb"))

def printDf():
  df = loadDataFrame()
  df = pd.DataFrame(df)
  print(df)
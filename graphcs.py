import numpy as np
import pandas as pd
import pickle as pk
import matplotlib.pyplot as plt

def generateQueryGraphics(opc):
    df = loadDataFrame()
    df = pd.DataFrame(data=df)
    df_transposed = df.T.rename(index={0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8',
                                       8: '9', 9: '10', 10: '11', 11: '12', 12: '13', 13: '14', 14: '15',
                                       15: '16', 16: '17', 17: '18', 18: '19', 19: '20', 20: '21', 21: '22',
                                       22: '23', 23: '24', 24: '25', 25: '26', 26: '27', 27: '28', 28: '29',
                                       29: 30, 30: 31})

    if opc == "dia":
        df_transposed.columns = ['Janeiro', 'Fevereiro', 'Março', 'Abril',
                'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        df_transposed.plot.barh(stacked=True)
        plt.show()

    elif opc == "mes":
        df['Total'] = df.sum(axis=1)
        df_rename = df['Total'].rename(index={0: 'Janeiro', 1: 'Fevereiro', 2: 'Março', 3: 'Abril', 4: 'Maio',
                                              5: 'Junho', 6:'Julho', 7: 'Agosto', 8: 'Setembro', 9: 'Outubro',
                                              10: 'Novembro', 11: 'Dezembro'})
        df_rename.plot.barh(stacked=True)
        plt.show()

def loadDataFrame():

  try:
    df = pk.load(open("dados//dataframe.pickle", "rb"))
  except:
    print("criando arquivo de pacientes")
    df = np.zeros((12, 31), dtype=int)
    pk.dump(df, open("dados//dataframe.pickle", "wb"))
  return df

def saveDataFrame(df):
  pk.dump(df, open("dados//dataframe.pickle", "wb"))


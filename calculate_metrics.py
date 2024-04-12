import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class calcular_valores():
   def __init__(self, df):
      self.df = df

   def analise_estatistica(self):
      media = self.df['totalFormatado'].mean()
      desvioPadrao = self.df['totalFormatado'].std()
      mediana = self.df['totalFormatado'].median()
      primeiroQuartil = self.df['totalFormatado'].quantile(0.25)
      terceiroQuartil = self.df['totalFormatado'].quantile(0.75)
      coeficienteVariacao = (desvioPadrao / media) * 100
      return media, desvioPadrao, mediana, primeiroQuartil, terceiroQuartil, coeficienteVariacao
    
   def plotar_distribuicao_normal(self):
      sns.set(style="whitegrid")
      plt.figure(figsize=(10, 6))
      sns.histplot(self.df['totalFormatado'], color='darkblue')
      plt.title('Distribuição Normal dos Índices')
      plt.xlabel('Valor')
      plt.ylabel('Frequência')
      plt.show()

   def identificar_outliers(self, primeiroQuartil, terceiroQuartil):
      interquartil = terceiroQuartil - primeiroQuartil
      lower_bound = primeiroQuartil - 1.5 * interquartil
      upper_bound = terceiroQuartil + 1.5 * interquartil
      outliers = self.df[(self.df['totalFormatado'] < lower_bound) | (self.df['totalFormatado'] > upper_bound)]
      return outliers

   def plotar_boxplot(self):
      plt.figure(figsize=(10, 6))
      sns.boxplot(x=self.df['totalFormatado'], color='darkblue')
      plt.title('Boxplot dos Índices')
      plt.xlabel('Índice')
      plt.show()

   def plotar_curva_indice_tempo(self):
      plt.figure(figsize=(10, 6))
      plt.plot(self.df['dataFormatado'], self.df['totalFormatado'], marker='o', linestyle='-', color='darkblue')
      plt.title('Curva de Índice vs Tempo')
      plt.xlabel('Data')
      plt.ylabel('Índice')
      plt.xticks(self.df['dataFormatado'][::12], rotation=45)
      plt.tight_layout()
      plt.show()

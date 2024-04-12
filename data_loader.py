import pandas as pd
import requests as req
from io import BytesIO

class excelReader:
    def __init__(self,url):
        self.url = url 

    def readExcel(self):
        try:
            response = req.get(self.url)
            # print(response) 

            if response.status_code == 200:
                content = response.content           
                df = pd.read_excel(BytesIO(content), sheet_name="Índice FipeZAP", header=3, usecols=['Data', 'Total'])
                ultimo_indice = df['Total'].last_valid_index()
                df = df.iloc[:ultimo_indice + 1]
                df['dataFormatado'] = pd.to_datetime(df['Data'])
                df['totalFormatado'] = df['Total'].round(2)
                df = df.drop(['Data', 'Total'], axis = 1)
                return df
            
            else:
                print("Erro ao baixar o arquivo. Código de status:", response.status_code)
                return None
            
        except Exception as ex:
            print("Ocorreu um erro ao abrir a planilha:", ex)
            return None
        
        
url = 'https://downloads.fipe.org.br/indices/fipezap/fipezap-serieshistoricas.xlsx'


call = excelReader(url)
df = call.readExcel()
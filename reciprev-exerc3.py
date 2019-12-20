import os
import sys
import matplotlib.pyplot as mpl #Biblioteca usada para plotar o grafico.

x = []
y = []

#Função para inverter a primeira posição com a segunda da data (Data do dataset no formato americano)
def reverse_date(date):
    data_splited = date.split("/")
    temp = data_splited[0]
    data_splited[0] = data_splited[1]
    data_splited[1] = temp
    return "{}/{}/{}".format(data_splited[0], data_splited[1], data_splited[2])

#Função para preparar os dados
death_date = {}
def prepare_data(date):
    date = reverse_date(date)
    if date in death_date:
        death_date[date] = death_date[date] + 1
    else:
        death_date[date] = 1

with open(os.path.join(sys.path[0], "caso-dengue2018.csv"), "r", encoding="utf8") as dset: #CSV de casos de dengue
    columns = dset.readline().split(";") #Primeira leitura para pegar as colunas
    line = dset.readline() #Segunda leitura para pegar os dados
    while line != "":
        data = line.split(";")
        if data[len(data) - 2] != "":
            prepare_data(data[len(data) - 2])
        
        line = dset.readline()

    for k, i in death_date.items():
        x.append(k)
        y.append(i)

mpl.plot(x, y)
mpl.title("Numero de Mortes por Data")
mpl.ylabel("Numero de Mortes")
mpl.xlabel("Data da Morte")

mpl.show()
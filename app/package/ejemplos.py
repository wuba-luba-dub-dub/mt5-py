#Abrir un archivo csv e imporimirlo
from datetime import date
from datetime import datetime

opened_file=open('AppleStore.csv')

from csv import reader
read_file=reader(opened_file)
apps_data=list(read_file)

print(len(apps_data))
print(apps_data[0])
print(apps_data[1:3])

#Creacion de datastore en variable de arreglo

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

for each_list in app_data_set:
    print(each_list)

#Fecha actual
date_now = str(datetime.now())
ano=date_now[0:4]
mes=date_now[5:7]
dia=date_now[8:10]
hora=date_now[11:13]
fecha=ano + ',' + mes + ',' + dia + ','+ hora
print(fecha)
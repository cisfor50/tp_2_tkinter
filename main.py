from tkinter import Tk, Frame, Label, Radiobutton, Button, Entry, StringVar, IntVar, messagebox
from calculos import mejorDisparo, promedioDisparo
import random
import csv
import openpyxl
from operator import itemgetter

#función para determinar el value del radio button
def sexo_value():
    resultado = 'F' if sexo.get() == 1 else 'M'
    return resultado

#funcion que ordena la lista de participantes por PROMEDIO para determinar el ganador
#cuando se presiona el botón ganador
def ganador():
    promedio_ordenado = sorted(participantes, key=itemgetter(9))
    messagebox.showinfo(title="GANADOR :)", message=f"El ganador es: {promedio_ordenado[0][1]} {promedio_ordenado[0][2]}, con el promedio de {promedio_ordenado[0][9]}. Felicitaciones!!!")

#lista de listas que guarda los datos de cada participante
participantes = []
def guardar():
    #tupla que almacena los values de los entrys disparos 1, 2 y 3.
    disparos = (float(entry_Disparo1.get()), float(entry_Disparo2.get()), float(entry_Disparo3.get()))
    #llama a la función mejor_disparo en el módulo calculos.py y retorna el mejor disparo del participante.
    mejor_disparo = mejorDisparo(disparos)
    #llama a la función promedio_disparo en el módulo calculos.py y retorna el promedio de los 3 disparos del participante.
    promedio_disparo = promedioDisparo(disparos)   

    #almaceno en variables los entrys de cada participante.
    numero_id = random.randrange(0,999)
    nombre = entry_Nombre.get()
    apellido = entry_Apellido.get()
    edad = entry_Edad.get()
    sexo = sexo_value()
    disparo1 = entry_Disparo1.get()
    disparo2 = entry_Disparo2.get()
    disparo3 = entry_Disparo3.get()
    mejor_disparo = mejor_disparo
    promedio_disparo = promedio_disparo  
    
    participante = [numero_id, nombre, apellido, edad, sexo, disparo1, disparo2, disparo3, mejor_disparo, promedio_disparo]
    participantes.append(participante)
    #llamo a la función que crea el csv cuando presiono el botón Guardar.
    participantes_csv()
    #limpio los campos para facilitar el ingreso de datos.
    limpiar_campos()


def participantes_csv():
    #guardo los participantes ordenados
    participantes_ordenados = sorted(participantes, key=itemgetter(8))
    # abro el csv en modo w+ 
    file = open('guardar_participantes.csv', 'w+', newline ='')     
    # escribo la data en el archivo 
    with file:     
        write = csv.writer(file) 
        write.writerows(participantes_ordenados) 

#limpia campos luego de guardar, mostrar ganador o exportar xslx
def limpiar_campos():
    entry_Nombre.delete(0, 'end')
    entry_Apellido.delete(0, 'end')
    entry_Edad.delete(0, 'end')
    entry_Disparo1.delete(0, 'end')
    entry_Disparo2.delete(0, 'end')
    entry_Disparo3.delete(0, 'end')

#crea el xlsx con los participantes
def exportar():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    #llamo al csv que cree en participantes_csv()
    file = open('guardar_participantes.csv')
    #primero appendeo los headers de cada columna
    headers = ['ID', 'Nombre', 'Apellido', 'Edad','Sexo', 'Disparo 1', 'Disparo 2', 'Disparo 3', 'Mejor disparo', 'Promedio']
    sheet.append(headers)
    #leo el csv y separo la data por comas
    reader = csv.reader(file, delimiter=',')
    #appendeo la data de participantes
    for row in reader:
        sheet.append(row)
    #guardo el xlsx con la data que registré en el csv
    workbook.save(filename='participantes.xlsx')
    #vuelvo a limpiar los campos para facilitar la continuación en la carga de datos
    limpiar_campos()

#Interfaz gráfica TKINTER
root = Tk()
root.title("Concurso de disparos")
root.geometry("350x320")

sexo = IntVar()

label_1 = Label(root, text= "Nombre", padx = 5, pady= 10, font= 'Arial 10')
label_1.grid(row=0, column=0)
entry_Nombre = Entry(root, width=30)
entry_Nombre.grid(row=0, column=1)

label_2 = Label(root, text= "Apellido", padx = 5, pady= 10, font= 'Arial 10')
label_2.grid(row=1, column=0)
entry_Apellido = Entry(root, width=30)
entry_Apellido.grid(row=1, column=1)

label_2 = Label(root, text= "Edad", padx = 5, pady= 10, font= 'Arial 10')
label_2.grid(row=2, column=0)
entry_Edad = Entry(root, width=30)
entry_Edad.grid(row=2, column=1)


rb_1 = Radiobutton(root, text="Femenino", value=1, variable=sexo, command=sexo_value)
rb_1.grid(row=3, column=0)
rb_2 = Radiobutton(root, text="Masculino", value=2, variable=sexo, command=sexo_value)
rb_2.grid(row=3, column=1)

label_3 = Label(root, text= "Disparo 1", padx = 5, pady= 10, font= 'Arial 10')
label_3.grid(row=4, column=0)
entry_Disparo1 = Entry(root, width=30)
entry_Disparo1.grid(row=4, column=1)

label_4 = Label(root, text= "Disparo 2", padx = 5, pady= 10, font= 'Arial 10')
label_4.grid(row=5, column=0)
entry_Disparo2 = Entry(root, width=30)
entry_Disparo2.grid(row=5, column=1)

label_5 = Label(root, text= "Disparo 3", padx = 5, pady= 10, font= 'Arial 10')
label_5.grid(row=6, column=0)
entry_Disparo3 = Entry(root, width=30)
entry_Disparo3.grid(row=6, column=1)

button_Guardar = Button(root, text= "Guardar", font="Arial 10", command = guardar)
button_Guardar.grid(row=7, column=0)
button_Ganador = Button(root, text= "Ganador", font="Arial 10", command = ganador)
button_Ganador.grid(row=7, column=1)
button_Exportar = Button(root, text= "Exportar xls", font="Arial 10", command= exportar)
button_Exportar.grid(row=7, column=2)


root.mainloop()

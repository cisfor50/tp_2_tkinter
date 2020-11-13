from tkinter import Tk, Frame, Label, Radiobutton, Button, Entry, StringVar, IntVar, messagebox
from calculos import mejorDisparo, promedioDisparo
import random

participantes = []
participante = dict()

def sexo_value():
    resultado = 'M' if sexo.get() == 1 else 'F'
    return resultado
  
def guardar():
  participante['numero_id'] = random.randrange(0,999)
  participante['nombre'] = entry_Nombre.get()
  participante['apellido'] = entry_Apellido.get()
  participante['edad'] = entry_Edad.get()
  participante['sexo'] = sexo_value()
  participante['disparo1'] = entry_Disparo1.get()
  participante['disparo2'] = entry_Disparo2.get()
  participante['disparo3'] = entry_Disparo3.get()
  participante['mejor_disparo'] = mejorDisparo
  participante['promedio_disparo'] = promedioDisparo  
  participantes.append(participante)






root = Tk()
root.title("Concurso de disparo")
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

button_Guardar = Button(root, text= "Guardar", font="Arial 10")
button_Guardar.grid(row=7, column=0)
button_Guardar = Button(root, text= "Ganador", font="Arial 10")
button_Guardar.grid(row=7, column=1)
button_Guardar = Button(root, text= "Exportar xls", font="Arial 10")
button_Guardar.grid(row=7, column=2)


root.mainloop()

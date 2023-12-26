from tkinter import *

root = Tk()
root.title('Hola mundo: Option menu')
root.geometry('500x500')
value = StringVar()

def enviar():
    l = Label(root, text=value.get())
    l.pack()

lista = [
    'Chanchito Feliz', 
    'Chanchito triste',
    'Chanchito emocionado'
]


    
value = StringVar()
value.set(lista[1])

drop = OptionMenu(root, value, *lista)
drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()
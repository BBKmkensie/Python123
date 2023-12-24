from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('500x500')

e = Entry(root, width=40)
e.pack()
e.insert(0, "Ingresa texto:")

def click():
    texto = e.get() #texto almacena texto pero label es donde se puede escriber abajo
    textvariable.set(texto)
    valor = textvariable.get()# varible valor, con el q almacena terxto
    print(valor)# te imprime lso valores en la terminal
    # l = Label(root, text=texto)
    # l.pack()
    e.delete(0, END)    
    # l.configure(text=texto)
    
btn = Button(root, text='click', command=click)
btn.pack()

textvariable = StringVar()

l = Label(root, textvariable=textvariable) # el label almacena text variable
l.pack()

root.mainloop()

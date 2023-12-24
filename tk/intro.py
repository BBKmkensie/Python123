from tkinter import  *

root =Tk()#llama a tk
root.title('Hola mundo')#mensaje en la ventana
root.geometry('500x500')#tamaño de la ventana

l1 = Label(root, text='Hola mundo!  primera etiqueta')
l2 = Label(root, text='Chao mundo! segunda etiqueta')
l3 = Label(root, text='')
# Label(root, text='Hola mundo! mi primera etiqueta').pack()

l1.grid(row=0, column=0)
l3.grid(row=1, column=1)
l2.grid(row=10, column=10)

# l1.pack()
# l2.pack()



root.mainloop()#ejecuta la ventana

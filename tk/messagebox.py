from tkinter import *
from tkinter import  messagebox

root = Tk()
root.title('Hola Mundo')

# def click():
#     messagebox.showwarning('Popup', 'Hola mundo!')
    
# def click():
#     messagebox.showinfo('Popup', 'Hola mundo!')
  
# def click():
#     messagebox.showerror('Popup', 'Hola mundo! :(')
  

# def click():
#     respuesta = messagebox.askquestion('Popup', 'Hola mundo!')
#     if respuesta == 'yes':
#         messagebox.showinfo('Respuesta', 'la respuesta fue ' + respuesta)
#     else:
#         messagebox.showinfo('Respuesta', ':( la respuesta fue ' + respuesta)

#uno de los favoritos
# def click():
#     respuesta = messagebox.askokcancel('Hola Mundo', 'Desea realizar una accion?')
#     if respuesta:
#         messagebox.showinfo('Hola Mundo', 'La respuesta fue OK')
#     else:
#         messagebox.showinfo('Hola Mundo','La respuesta fue Cancel')


def click():
    respuesta = messagebox.askyesno('Hola Mundo', 'Desea realizar una accion?')
    if respuesta:
        messagebox.showinfo('Hola Mundo', 'La respuesta fue YES')
    else:
        messagebox.showinfo('Hola Mundo','La respuesta fue No')

btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()

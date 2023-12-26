from  tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola Mundo')

#solucion 1
# def open():
#     img = ImageTk.PhotoImage(Image.open('images/1.png'))
#     top = Toplevel()
#     top.title('Hola mundo, nueva ventana')
#     l = Label(top, text='Soy un texto en una segunda ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()
    
# solucion2
# def open():
#     global img
#     img = ImageTk.PhotoImage(Image.open('images/1.png'))
#     top = Toplevel()
#     top.title('Hola mundo, nueva ventana')
#     l = Label(top, text='Soy un texto en una segunda ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
# btn = Button(root, text='Click', command=open).pack()

# solucion3
def open(img):
    top = Toplevel()
    top.title('Hola mundo, nueva ventana')
    l = Label(top, text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()



img = ImageTk.PhotoImage(Image.open('images/1.png'))
btn = Button(root, text='Click', command=lambda: open(img)).pack()
 
root.mainloop()

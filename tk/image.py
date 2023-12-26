from tkinter import *
from PIL import ImageTk, Image
 
root = Tk()
root.title('Hola Mundo')

# imagen = Image.open('cr7siiu.png')
# imagen.show()

img = ImageTk.PhotoImage(Image.open('cr7siiu.png'))
l = Label(image=img)
l.pack()

root.mainloop()
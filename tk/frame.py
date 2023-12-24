from tkinter import * 

root = Tk()
root.title('Hola mundo')
root.geometry('738x544')# misma medida que el melchor

# frame  = LabelFrame(root, text='Login', padx= 10, pady=10, borderwidth=10)
frame  = LabelFrame(root, padx= 10, pady=10, borderwidth=10)  #no dice login
frame.pack(padx=50, pady=50)

frame.pack()
l = Label(frame, text='Estoy dentro de un frame')
# l.pack(padx=60, pady=60)
btn = Button(frame, text='Salir', command=root.quit)
l.pack()
btn.pack()

root.mainloop()

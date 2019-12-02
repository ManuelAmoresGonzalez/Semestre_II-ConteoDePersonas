from tkinter import filedialog
from tkinter import *

def ingresar():
    #Aquí se piensa acceder a la terminal desde código
    tk.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp4 files","*.mp4"),("all files","*.*")))
    print (tk.filename) #imprime la ruta del video 
    
tk=Tk() #ventana padre
tk.config (background="gray") #fondo gris
tk.title("Selección del video") #título
#tk.geometry ("1200x800") #el tamaño
w, h = tk.winfo_screenwidth(), tk.winfo_screenheight()
tk.geometry("%dx%d+0+0" % (w, h)) #fullscreen

lbl1=Label (tk, text="Seleccione el video que desea escanear", font=("Times New Roman", 16, "bold"), bg="white", fg="black").pack()

#label1=Label (tk, text="Seleccione el video que desea escanear", font="Arial, 16").pack()

Button (tk, text="Seleccionar", font=("Times New Roman", 16, "bold"), bg="white", fg="black", command = lambda:ingresar()).pack() #btn seleccionar

tk.mainloop () #para que no se cierre

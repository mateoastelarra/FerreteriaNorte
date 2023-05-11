from lib2to3.pgen2.pgen import DFAState
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
#from readText import get_orders
#from mail_compras import send_email
import time
import datetime


# Define variable to upload txt file with all orders
orders = []

# Get current time
current_time = datetime.datetime.now()
months = {1:"Enero", 2: "Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10: "Octubre", 11:"Noviembre", 12:"Diciembre"}
month = months[current_time.month]


def open_file():
    global orders
    file_path = askopenfile(mode='r', filetypes = [("Excel Files", "*.xlsx")])
    #orders = get_orders(file_path.name)


#Podría ir procesar datos y enviar mail como uno o dos botones en vez de subir archivo
def uploadFiles():
    pb1 = Progressbar(
        app, 
        orient=HORIZONTAL, 
        length=200, 
        mode='determinate'
        )
    pb1.grid(row=3, columnspan=80)
    for i in range(5):
        app.update_idletasks()
        pb1['value'] += 20
        time.sleep(0.1)
    pb1.destroy()
    Label(app, text="Se subió el archivo correctamente!", foreground='green').grid(row = 4, column = 0, columnspan=80)


def Update_prices():
    print("ok")


# def focus_mail_prueba_entry(_):
#     entry_mail_prueba.delete(0, END)
#     entry_mail_prueba.config(foreground='black')

# def focus_mail_salida(_):
#     entry_mail_prueba.delete(0, END)



app = Tk() 
app.title('Registro y Actualización de precios')
app.geometry('420x120') 

var_mail_prueba = StringVar()    

# subarch = Label(
#     app, 
#     text='Subir la planilla de ' + month #agregar mes menos 1 automáticamente? 
#     )
# subarch.grid(row=1, column=0, padx=10)

upload_file_proveedor = Button(
    app, 
    text ='Subir la Planilla del proveedor', 
    command = open_file
    ) 
upload_file_proveedor.grid(row=2, column=1, columnspan=3, padx=10)

subarchbtn = Button(
    app, 
    text ='Subir la Planilla de la Ferretaría', 
    command = open_file
    ) 
subarchbtn.grid(row=3, column=1, columnspan=3)



# mailPrueba = Button(
#     app, text = "Mandar Mail de Prueba",
#     command = MandarMailPrueba
# )
# mailPrueba.grid(row = 2, column = 1, pady = 10)

upld = Button(
    app, 
    text='Actualizar precios', 
    command= Update_prices
    )
# Acá podrían específicar la columna donde está el código de los productos
upld.grid(row = 4, column = 4, pady=20, padx=60)
entry_mail_prueba = Entry(app, textvariable = var_mail_prueba, width = 35, foreground = "grey")
entry_mail_prueba.grid(row = 2,column = 4, pady = 10)
entry_mail_prueba.insert(0, "Columna de códigos de productos")

#entry_mail_prueba.bind("<FocusIn>", focus_mail_prueba_entry)
app.mainloop()
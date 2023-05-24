
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import os
from helpers import update_prices

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox

dir_path = os.getcwd()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / os.path.join(dir_path,"FerreteriaNorte", "assets", "frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#3A7FF6")
window.title("Actualización de Precios")

#función para solicitar apertura de archivo
def select_file_proveedor():
    global file_path_proveedor
    # Abre el cuadro de diálogo para seleccionar un archivo
    file_path_proveedor = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
    
    # Mostrar mensaje de confirmación con icono
    messagebox.showinfo("Archivo cargado", "El archivo se ha cargado con éxito.")

    # Muestra la ruta del archivo seleccionado en la consola
    print("Archivo seleccionado:", file_path_proveedor)
def select_file_ferr():
    global file_path_ferrreteria
    # Abre el cuadro de diálogo para seleccionar un archivo
    file_path_ferrreteria = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])

    # Mostrar mensaje de confirmación con icono
    messagebox.showinfo("Archivo cargado", "El archivo se ha cargado con éxito.")

    # Muestra la ruta del archivo seleccionado en la consola
    print("Archivo seleccionado:", file_path_ferrreteria)
#función para obtener las columnas de las distintas planillas, quizás tengan que ser 4 funciones distintas.
def get_values():
    column_code_prov=entry_1.get()
    column_price_prov=entry_2.get()
    column_code_local=entry_3.get()
    column_price_local=entry_4.get()
    update_prices(file_path_proveedor, file_path_ferrreteria, column_code_prov, column_price_prov, column_code_local, column_price_local)
    print("listo")
    
canvas = Canvas(
    window,
    bg = "#3A7FF6",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    431.0,
    0.0,
    862.0,
    519.0,
    fill="#FCFCFC",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= get_values,
    relief="flat"
)
button_1.place(
    x=557.0,
    y=436.0,
    width=180.0,
    height=55.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    558.0,
    213.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D8DDE9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=493.0,
    y=198.0,
    width=130.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    739.0,
    213.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D8DDE9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=674.0,
    y=198.0,
    width=130.0,
    height=28.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=select_file_proveedor,
    relief="flat"
)
button_2.place(
    x=474.0,
    y=76.0,
    width=345.0,
    height=61.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=select_file_ferr,
    relief="flat"
)
button_3.place(
    x=474.0,
    y=260.0,
    width=345.0,
    height=61.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=select_file_proveedor,
    relief="flat"
)
button_4.place(
    x=779.0,
    y=96.0,
    width=24.0,
    height=22.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=select_file_ferr,
    relief="flat"
)
button_5.place(
    x=779.0,
    y=280.0,
    width=24.0,
    height=22.0
)

canvas.create_text(
    478.0,
    28.0,
    anchor="nw",
    text="Cargá los archivos “.xlsx”",
    fill="#505485",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    43.0,
    239.0,
    anchor="nw",
    text="Usamos un sistema de automatización",
    fill="#FCFCFC",
    font=("RobotoRoman Regular", 18 * -1)
)

canvas.create_text(
    43.0,
    265.0,
    anchor="nw",
    text="basado en Python para actualizar precios",
    fill="#FCFCFC",
    font=("RobotoRoman Regular", 18 * -1)
)

canvas.create_text(
    43.0,
    291.0,
    anchor="nw",
    text="de sus proveedores. ",
    fill="#FCFCFC",
    font=("RobotoRoman Regular", 18 * -1)
)

canvas.create_text(
    43.0,
    350.0,
    anchor="nw",
    text="Se busca una herramienta que eficientice ",
    fill="#FCFCFC",
    font=("RobotoRoman Regular", 18 * -1)
)

canvas.create_text(
    527.0,
    145.0,
    anchor="nw",
    text="Detallá en que columna están:",
    fill="#000000",
    font=("RobotoRoman Regular", 18 * -1)
)

canvas.create_text(
    505.0,
    176.0,
    anchor="nw",
    text="Código producto",
    fill="#000000",
    font=("RobotoRoman Regular", 15 * -1)
)

canvas.create_text(
    680.0,
    176.0,
    anchor="nw",
    text="Precio a actualizar",
    fill="#000000",
    font=("RobotoRoman Regular", 15 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    558.0,
    404.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D8DDE9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=493.0,
    y=389.0,
    width=130.0,
    height=28.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    739.0,
    404.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D8DDE9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=674.0,
    y=389.0,
    width=130.0,
    height=28.0
)

canvas.create_text(
    527.0,
    336.0,
    anchor="nw",
    text="Detallá en que columna están:",
    fill="#000000",
    font=("RobotoRoman Regular", 18 * -1)
)

canvas.create_text(
    505.0,
    367.0,
    anchor="nw",
    text="Código producto",
    fill="#000000",
    font=("RobotoRoman Regular", 15 * -1)
)

canvas.create_text(
    680.0,
    367.0,
    anchor="nw",
    text="Precio a actualizar",
    fill="#000000",
    font=("RobotoRoman Regular", 15 * -1)
)

canvas.create_text(
    43.0,
    376.0,
    anchor="nw",
    text="y facilite estos preoceso en su empresa. ",
    fill="#FCFCFC",
    font=("RobotoRoman Regular", 18 * -1)
)

canvas.create_rectangle(
    43.0,
    208.0,
    103.0,
    213.0,
    fill="#FCFCFC",
    outline="")

canvas.create_text(
    43.0,
    170.0,
    anchor="nw",
    text="actualización de precios.",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    43.0,
    137.0,
    anchor="nw",
    text="Bienvenido a la App de ",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    220.0,
    56.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()

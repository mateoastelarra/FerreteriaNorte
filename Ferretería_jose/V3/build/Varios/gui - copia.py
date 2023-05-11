
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk #agregué para editar

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Jose\Desktop\python\Ferretería\V3\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#3A7FF6")


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
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=557.0,
    y=401.0,
    width=180.0,
    height=55.0
)
# lo siguiente agregué también
def handle_focus_in(_):
    entry_1.delete(0, tk.END)
    entry_1.config(fg='black')

def handle_focus_out(_):
    entry_1.delete(0, tk.END)
    entry_1.config(fg='grey')
    entry_1.insert(0, "Detalle en que columna está el código del producto")

def handle_enter(txt):
    print(entry_1.get())
    handle_focus_out('dummy')

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    650.5,
    329.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D8DDE9",
    #fg="#000716",
    fg="grey",
    highlightthickness=0
)
entry_1.insert(
    0, "Detalle en que columna está el código del producto"
)
entry_1.bind("<FocusIn>", handle_focus_in)
entry_1.bind("<FocusOut>", handle_focus_out)
entry_1.bind("<Return>", handle_enter)

entry_1.place(
    x=502.0,
    y=299.0,
    width=297.0,
    height=59.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=478.0,
    y=137.0,
    width=345.0,
    height=61.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=478.0,
    y=218.0,
    width=345.0,
    height=61.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=783.0,
    y=157.0,
    width=24.0,
    height=22.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=783.0,
    y=238.0,
    width=24.0,
    height=22.0
)

canvas.create_text(
    482.0,
    74.0,
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

#temas a tener en cuenta: 
#  1- en el entry se puede tomar el text con enter (sin espefíciar y/o con el boton actualizar)
#  2- habría que pensar una manera de que la app no se pueda clonar. Que en este caso la ferretería
#  no comparta la app.
#  3- Es confuso la columna de que planilla hay que escribir, quizás ponerlo debajo de la de proveedor o, mejor
#  invertir el orden primero que se suba la de la ferretería, segunda la del proveedor y así.


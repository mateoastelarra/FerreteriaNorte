
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Jose\Desktop\python\Ferretería\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Ferretería Norte")
window.geometry("394x166")
window.configure(bg = "#786BC9")


canvas = Canvas(
    window,
    bg = "#786BC9",
    height = 166,
    width = 394,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    197.0,
    0.0,
    394.0,
    166.0,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    96.0,
    90.0,
    image=image_image_1
)

canvas.create_rectangle(
    13.0,
    11.0,
    178.0,
    32.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    18.0,
    14.0,
    anchor="nw",
    text="Actualización de productos",
    fill="#000000",
    font=("Inter Regular", 12 * -1)
)

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
    x=238.0,
    y=117.0,
    width=115.0,
    height=30.0
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
    x=238.0,
    y=69.0,
    width=115.0,
    height=30.0
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
    x=238.0,
    y=21.0,
    width=115.0,
    height=30.0
)
window.resizable(False, False)
window.mainloop()

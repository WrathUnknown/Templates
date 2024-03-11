
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\your-username\Documents\My Web Sites\WebSite1\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#24A0FA")


canvas = Canvas(
    window,
    bg = "#24A0FA",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    430.9999999999999,
    0.0,
    861.9999999999999,
    519.0,
    fill="#F8F8F6",
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
    x=556.9999999999999,
    y=401.0,
    width=180.0,
    height=55.0
)

canvas.create_text(
    39.999999999999886,
    10.000000000000007,
    anchor="nw",
    text="Home Page",
    fill="#333333",
    font=("RubikRoman Bold", 32 * -1)
)

canvas.create_text(
    481.9999999999999,
    74.0,
    anchor="nw",
    text="Enter your details:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_rectangle(
    39.999999999999886,
    57.00000000000001,
    99.99999999999989,
    62.00000000000001,
    fill="#F1F5FF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    650.4999999999999,
    167.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#24A0FA",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=489.9999999999999,
    y=137.0,
    width=321.0,
    height=59.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    650.4999999999999,
    248.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#24A0FA",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=489.9999999999999,
    y=218.0,
    width=321.0,
    height=59.0
)

canvas.create_text(
    39.999999999999886,
    92.0,
    anchor="nw",
    text="In this app you will find weather forecasts, reports and advice!\n\n",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    39.999999999999886,
    257.0,
    anchor="nw",
    text="Try the tracking tool today!",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)
window.resizable(False, False)
window.mainloop()

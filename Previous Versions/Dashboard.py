
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\your-username\Documents\My Web Sites\WebSite1\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
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
    x=671.0,
    y=440.0,
    width=180.0,
    height=55.0
)

canvas.create_text(
    21.0,
    14.0,
    anchor="nw",
    text="Weather Dashboard",
    fill="#333333",
    font=("RubikRoman Bold", 32 * -1)
)

canvas.create_text(
    21.0,
    211.0,
    anchor="nw",
    text="19 °C",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    19.0,
    246.0,
    anchor="nw",
    text="Monday:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    478.0,
    5.0,
    anchor="nw",
    text="Week:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    70.0,
    285.0,
    anchor="nw",
    text="Rain: 40%",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_rectangle(
    21.0,
    63.0,
    81.0,
    68.0,
    fill="#24A0FA",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    196.0,
    139.0,
    image=image_image_1
)

canvas.create_rectangle(
    19.0,
    279.0,
    59.0,
    319.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    19.0,
    336.0,
    415.0,
    510.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    477.0,
    44.0,
    559.0,
    190.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    606.0,
    44.0,
    688.0,
    190.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    748.0,
    44.0,
    830.0,
    190.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    489.0,
    52.0,
    anchor="nw",
    text="Mon:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    622.0,
    54.0,
    anchor="nw",
    text="Tue:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    761.0,
    54.0,
    anchor="nw",
    text="Wed:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_rectangle(
    484.0,
    99.0,
    551.0,
    163.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    614.0,
    99.0,
    681.0,
    166.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    751.0,
    96.0,
    826.5723876953125,
    163.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    477.0,
    223.0,
    559.0,
    369.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    607.0,
    223.0,
    689.0,
    369.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    472.0,
    382.0,
    554.0,
    510.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    744.0,
    223.0,
    826.0,
    369.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    489.0,
    232.0,
    anchor="nw",
    text="Thu:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    486.0,
    388.0,
    anchor="nw",
    text="Sun:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    627.0,
    232.0,
    anchor="nw",
    text="Fri:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_text(
    762.0,
    232.0,
    anchor="nw",
    text="Sat:",
    fill="#333333",
    font=("RubikRoman Bold", 24 * -1)
)

canvas.create_rectangle(
    492.0,
    262.0,
    547.301586151123,
    329.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    614.0,
    273.0,
    681.0,
    340.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    749.0,
    269.0,
    824.5723876953125,
    336.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    479.0,
    423.0,
    547.0983581542969,
    490.0,
    fill="#FFFFFF",
    outline="")
window.resizable(False, False)
window.mainloop()

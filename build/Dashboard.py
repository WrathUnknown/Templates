import webbrowser
from pathlib import Path
# !!! Note: Most of the code will be repeated and thus will not be commented on !!!
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage #Imports


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\your-username\OneDrive\Documents\Github\OCC-Mock\build\assets\frame1") #Change this path to wherever frame1 is located on your pc.


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def callback_page(url):
    webbrowser.open_new(r'C:\\Users\\your-username\\OneDrive\\Documents\\Github\\OCC-Mock\\build\\Home-Page.py') #Will open the home-page file, will be relevant when clicking the buttons available. Make sure to change this path!!!

def callback_web(url):
    webbrowser.open_new(url) #Does the same action as line 16 but instead opens up your browser to direct to a relevant website.

window = Tk()

window.geometry("862x519") #Size of window.
window.configure(bg = "#FFFFFF")


canvas = Canvas( #Creates a canvas (all the code below is for the figma designs).
    window,
    bg = "#FFFFFF",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle( #Creates a rectangle and places it in the relevant place.
    431.0,
    0.0,
    862.0,
    519.0,
    fill="#F8F8F6",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png")) #This will be used in the python files as a functioning button, the image is what it will look like essentially.
button_1 = Button( #Creates a button.
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: callback_page (r'C:\\Users\\your-username\\OneDrive\\Documents\\Github\\OCC-Mock\\build\\Home-Page.py'), #This line means that if a the button is clicked it will direct to the other python file "Home-Page". Make sure to change this path!!!
    relief="flat"
)
button_1.place( #Sets the place of the button.
    x=631.0,
    y=388.0,
    width=180.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: callback_web ('https://www.gov.uk/government/news/cold-health-alerts-issued-by-ukhsa-and-the-met-office'),
    relief="flat"
)
button_2.place(
    x=631.0,
    y=457.0,
    width=180.0,
    height=55.0
)

canvas.create_text( #Creates some text.
    107.0,
    5.0,
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
    107.0,
    49.0,
    167.0,
    54.0,
    fill="#24A0FA",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png")) #Allows the relevant image to be used in the program.
image_1 = canvas.create_image( #Creates the image.
    196.0,
    139.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    39.0,
    299.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    217.0,
    423.0,
    image=image_image_3
)

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

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    517.0,
    131.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    647.0,
    132.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    788.0,
    129.0,
    image=image_image_6
)

canvas.create_rectangle(
    478.0,
    223.0,
    560.0,
    369.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    8.0,
    7.0,
    90.0,
    153.0,
    fill="#E5E5E5",
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

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    519.0,
    295.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    647.0,
    306.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    786.0,
    302.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    513.0,
    456.0,
    image=image_image_10
)

button_image_3 = PhotoImage( #Behaves the same way as the previous button/s.
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: callback_page (r'C:\\Users\\your-username\\OneDrive\\Documents\\Github\\OCC-Mock\\build\\Home-Page.py'), #Make sure to change this path!!!
    relief="flat"
)
button_3.place(
    x=17.0,
    y=11.0,
    width=62.0,
    height=57.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: callback_web ('https://www.metoffice.gov.uk/weather/warnings-and-advice/seasonal-advice/health-wellbeing/stay-well-in-winter/stay-well-in-winter'), #This behaves in the same way as the other actions but instead redirects you to a web page.
    relief="flat"
)
button_4.place(
    x=16.0,
    y=85.0,
    width=63.0,
    height=55.0
)
window.resizable(False, False)
window.mainloop()

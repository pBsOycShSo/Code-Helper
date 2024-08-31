import os
import tkinter
import keyboard
import customtkinter as ctk
from customtkinter import CTkLabel, CTkTextbox, CTkButton

app = ctk.CTk()
app.geometry("450x370")
app.iconbitmap("CustomTkinter_icon_Windows.ico")
ctk.set_appearance_mode("dark")
b = 0
dire = os.getcwd()
f = dire + "\\keys.k"


def file_open():
    txt_edit.delete(1.0, tkinter.END)
    with open(f, "r") as input_file:
        txt = input_file.read()
        txt_edit.insert(tkinter.END, txt)
    app.title(f"</CH> - {f}")


def run():
    global b
    with open(f, "w") as output_file:
        text = txt_edit.get(1.0, tkinter.END)
        output_file.write(text)
    if b < 1:
        try:
            file = open("keys.k")
            for line in file:
                if line.startswith("key"):
                    li = line.replace("\n", "")
                    keys = li.split(",")
                    keyboard.add_abbreviation(f'{keys[1]}', f'{keys[2]}', True)
                    b = 2
                    b1.configure(app, text="Stop", hover_color="red")

        except IndexError as error:
            f2 = CTkLabel(app, width=378, height=330, bg_color="transparent", text=f'{error}')
            f2.place(x=200, y=60)
    else:
        with open(f, "w") as output_file:
            text = txt_edit.get(1.0, tkinter.END)
            output_file.write(text)
        app.destroy()


txt_edit = CTkTextbox(app, width=450, height=370, font=('Lithos Pro', 20))
txt_edit.grid(sticky="ns")
file_open()
b1 = CTkButton(app, text="Start", width=140, height=28, corner_radius=20, border_width=1, bg_color="transparent",
               fg_color="transparent", hover_color="gray", font=("Bauhaus 93", 20 * -1), text_color="white",
               command=run)

b1.place(x=150, y=300)
app.resizable(False, False)
app.mainloop()

import os
import tkinter

import customtkinter as ctk
import keyboard
from customtkinter import CTkLabel, CTkTextbox, CTkButton

app = ctk.CTk()
app.geometry("450x370")
ctk.set_appearance_mode("dark")
b = 0
dire = os.getcwd()
f = dire + "\\keys.k"


def file_open():
    global b1
    txt_edit.delete(1.0, tkinter.END)
    b1 = CTkButton(app, text="Start", width=140, height=28, corner_radius=20, border_width=1, bg_color="transparent",
                   fg_color="transparent", hover_color="gray", font=("Bauhaus 93", 20 * -1), text_color="white",
                   command=run)
    try:
        with open(f, "r") as input_file:
            txt = input_file.read()
            txt_edit.insert(tkinter.END, txt)
        app.title(f"</CH> - {f}")
        b1.place(x=150, y=300)

    except Exception:
        f2 = CTkLabel(app, width=450, height=370, bg_color="transparent", text="[ key.k ] file is missing!",
                      font=('Lithos Pro', 20))
        f2.place(x=0, y=0)


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

        except Exception as error:
            f2 = CTkLabel(app, width=450, height=370, bg_color="transparent", text=f'{error}', font=('Lithos Pro', 20))
            f2.place(x=0, y=0)
    else:
        with open(f, "w") as output_file:
            text = txt_edit.get(1.0, tkinter.END)
            output_file.write(text)
        app.destroy()


txt_edit = CTkTextbox(app, width=450, height=370, font=('Lithos Pro', 20))
txt_edit.grid(sticky="ns")
file_open()

app.resizable(False, False)
app.mainloop()

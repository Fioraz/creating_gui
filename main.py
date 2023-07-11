from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=20, pady=20)

text_box = Entry()
text_box.grid(column=1, row=0)

label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)

label_2 = Label(text="0")
label_2.grid(column=1, row=1)

label_3 = Label(text="Miles")
label_3.grid(column=2, row=0)

label_4 = Label(text="Km")
label_4.grid(column=2, row=1)


def button_clicked():
    kilometres = round(float(text_box.get()) * 1.60934)
    label_2.config(text=kilometres)

# Button
button = Button(text="Convert", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
from tkinter import *

# Create window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Create Labels
label = Label(text="Hello!", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)  # Need pack() to display the label on window - by default it displays on top
label.config(padx=50, pady=50)

# Entry
input_text = Entry(width=10)
input_text.grid(column=3, row=2)


# Create button click event
def button_clicked():
    label.config(text=input_text.get())


# Button
button_1 = Button(text="Click Me", command=button_clicked)
button_1.grid(column=1, row=1)


# Button 2
button_2 = Button(text="Click Me", command=button_clicked)
button_2.grid(column=2, row=0)




window.mainloop()

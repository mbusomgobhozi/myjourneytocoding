from tkinter import *


# create a function that converts the user input
def conversion():
    convert = float(entry.get())
    answer = convert * 1.689
    converted["text"] = answer


# window creation
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# first row will be the text input and a label (the metric)
entry = Entry(width=10)
entry.grid(column=1, row=0)

label = Label(text="Miles")
label.grid(column=2, row=0)

# now for the second row which will be two text columns and one output column
is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

converted = Label(text="0")
converted.grid(column=1, row=1)

miles = Label(text="Km")
miles.grid(column=2, row=1)

# now for the button that will initiate the conversion
button = Button(text="Calculate", command=conversion)
button.grid(column=1, row=2)

window.mainloop()

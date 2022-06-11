from tkinter import *
from tkinter import colorchooser

root = Tk()

root.title("Color Picker")
root.geometry("400x400")

def color():

    customcolor = colorchooser.askcolor()[1]
    labelPreview = Label(root, text="Color Preview", font=("Helvetica", 32), bg=customcolor).pack()
    label = Label(root, text="Hex Color Code: " + customcolor).pack()

callcolorpicker = Button(root, text="Pick A Color", command=color).pack()

root.mainloop()
from tkinter import *

window = Tk()
window.title("Mile to km converter")
window.minsize(height=100, width=300)
window.config(padx= 20, pady = 20)

input = Entry(width=8)
input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

miles_answer_label = Label(text="0")
miles_answer_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

def convert_unit():
    miles = float(input.get())
    km = round(1.61 * miles, 2)
    miles_answer_label.config(text=str(km))


button = Button(text="Calculate", command=convert_unit)
button.grid(row=2, column=1)






window.mainloop()
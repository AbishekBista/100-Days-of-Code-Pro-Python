import tkinter

window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="Labels")
my_label.grid(column=0, row=0)

def button_clicked():
    input = entry.get()
    my_label["text"] = input

button = tkinter.Button(text="Press Me", command=button_clicked)
button.grid(column=1, row=1)

entry = tkinter.Entry(width = 10)
entry.grid(row=2, column=3)

new_button = tkinter.Button(text="New button")
new_button.grid(row=0, column=2)


window.mainloop()
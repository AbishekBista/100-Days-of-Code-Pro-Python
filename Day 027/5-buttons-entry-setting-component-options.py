import tkinter

window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Labels")
my_label.pack()

my_label["text"] = "GUI Label"
my_label.config(text="New label")

def button_clicked():
    input = entry.get()
    my_label["text"] = input

button = tkinter.Button(text="Press Me", command=button_clicked)
button.pack()

entry = tkinter.Entry(width = 10)
entry.pack()


window.mainloop()
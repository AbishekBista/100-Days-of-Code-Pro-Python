import tkinter
window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="Labels")
my_label.pack()

my_label["text"] = "GUI Label"
my_label.config(text="New label")

# Button
def button_clicked():
    input = entry.get()
    my_label["text"] = input

button = tkinter.Button(text="Press Me", command=button_clicked)
button.pack()

# Input field
entry = tkinter.Entry(width = 30)
entry.insert(tkinter.END, "Hello there")
entry.pack()

# Text field
text = tkinter.Text(height=5, width=30)
text.focus()
text.insert(tkinter.END, "Example of multi-line text entry")
print(text.get("1.0", tkinter.END))
text.pack()

# Spin box
def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton

def checkbutton_used():
    print(checked_state.get())

checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?",
variable = checked_state,
command = checkbutton_used)
checkbutton.pack()


# Radio buttons
def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)

radiobutton1.pack()
radiobutton2.pack()

# List box

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Banana", "Cherry"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()





window.mainloop()
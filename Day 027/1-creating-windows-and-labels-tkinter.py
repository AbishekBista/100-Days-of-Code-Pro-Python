import tkinter

window = tkinter.Tk()
window.title("Mario")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text='Label', font=("Arial", 24, "normal"))
my_label.pack(expand=True) # add to window and center it


window.mainloop()
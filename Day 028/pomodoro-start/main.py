from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps %2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark.config(text=checkmark.cget("text") + "✅")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
timer_label = Label(text="Timer", font=(FONT_NAME, 36), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Tomato Image and Counter
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width = 208, height = 224, bg=YELLOW, highlightthickness=0)
canvas.create_image(104, 112, image=tomato_img)
timer_text = canvas.create_text(104, 130, text="25:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)

# Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Check mark
checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "normal"))
checkmark.grid(row=3, column=1)


window.mainloop()
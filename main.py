import tkinter
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
timer= None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_count,text="25:00")
    reps = 0
    label_checkmark.config(text="")
    window.config(bg=YELLOW)
    canvas.configure(bg=YELLOW)
    label_checkmark.config(bg=YELLOW)
    label_timer.config(text="TIMER", fg=GREEN, bg=YELLOW)

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        window.config(bg = RED)
        canvas.configure(bg=RED)
        label_checkmark.config(bg=RED)
        label_timer.config(text="BREAK",fg="white",bg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        window.config(bg=PINK)
        canvas.configure(bg=PINK)
        label_checkmark.config(bg=PINK)
        label_timer.config(text="BREAK",fg="white",bg=PINK)
    else:
        count_down(WORK_MIN * 60)
        window.config(bg=YELLOW)
        canvas.configure(bg=YELLOW)
        label_checkmark.config(bg=YELLOW)
        label_timer.config(text="WORK",fg=GREEN,bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_count, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        label_checkmark.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx = 100, pady = 20, bg=YELLOW)

canvas = tkinter.Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato_img)
timer_count = canvas.create_text(100,135,text = "25:00", font =(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1,column=1)

label_timer = tkinter.Label(text = "TIMER", fg = GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
label_timer.grid(row=0,column=1)

button_start = tkinter.Button(text = "start", command= start_timer)
button_start.grid(row=2,column=0)

button_reset = tkinter.Button(text = "reset", command= reset_timer)
button_reset.grid(row=2,column=2)

label_checkmark = tkinter.Label(fg=GREEN, bg=YELLOW)
label_checkmark.grid(row=3,column=1)

window.mainloop()
import tkinter
import math
from tkinter import *
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
timer_id = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer_id

    if timer_id:
        window.after_cancel(timer_id)
        timer_id = None

    reps = 0

    canvas.itemconfig(timer_text, text="00:00")
    my_label_timer.config(text="Timer", fg=GREEN)
    my_label_tick.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        my_label_timer.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        my_label_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        my_label_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_id
    count_minutes = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text,text= f"{count_minutes}:{count_seconds}")
    if count > 0:
        timer_id = window.after(1000,count_down,count-1)
    else:
        timer()
        marks = ""
        work_sessions = reps // 2

        for _ in range(work_sessions):
            marks += "✓"

        my_label_tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Tomodo Game")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg= YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image = image)
timer_text = canvas.create_text(100,112,text="00:00",fill='white',font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)
# count_down(5)



my_label_timer = tkinter.Label(text='Timer',fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,'bold'))
my_label_timer.grid(row=0,column=1)
my_label_tick = tkinter.Label(fg=GREEN,bg=YELLOW)
my_label_tick.grid(column=1,row=2)

button_start = Button(text='Start',command=timer)
button_start.grid(row=2,column=0)
button_reset = Button(text='Reset',command=reset_timer)
button_reset.grid(row=2,column=3)


window.mainloop()

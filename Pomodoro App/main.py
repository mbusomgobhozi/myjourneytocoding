from tkinter import *
import time
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# recursive algorithim
def countdown(count):
    # rount down
    count_min = math.floor(count / 60)
    # seconds the remainder of the above code
    count_sec = count % 60

    # this is dynamic typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(25000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
            check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "normal"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
# create a timer text variable so we can edit the time in the apple
timer_txt = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)


window.mainloop()

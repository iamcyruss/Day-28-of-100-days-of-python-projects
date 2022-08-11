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
reps = 0
work = 0
breaks = 0
timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- # 
# this is being called by the start button 5 * 60 and passes it to countdown function
def start_timer():
    global reps
    reps += 1
    """
    below is my solution. I think ti would work just fine but teachers solution was diff.
    if reps <= 4:
        countdown(WORK_MIN * 60)
        time.sleep(1)
        countdown(SHORT_BREAK_MIN * 60)
        reps += 1
    elif reps == 5:
        countdown(LONG_BREAK_MIN * 60)
    """
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # reps % 8 has no remainder
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    # reps % 2 mean they are even
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        timer_label.config(text="Work", fg=GREEN)
        global work
        work += 1
        check_label.config(text=f"Work session {str(work)} in progress.")
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# countdown takes value from start_timer and breaks it into minutes and counts down
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{str(count_sec)}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # this line below is what actually does the countdown
        timer = window.after(1000, countdown, count - 1)
    # this else restarts the next timer once it hits 0
    else:
        start_timer()
        window.lift()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        if reps % 2 == 0:
            global breaks
            breaks += 1
            check_label.config(text=f"✔ Work session {str(breaks)} complete. Break time.")


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    # the hardest part of resetting is to stop the count down
    # we need to stop this line of code
    # window.after(1000, countdown, count - 1)
    # the way to do that is with the after_cancel() method
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
    check_label.config(text="")
    global reps, breaks, work
    reps = 0
    breaks = 0
    work = 0

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Work Timer")
window.config(padx=100, pady=50, bg=YELLOW)

image = PhotoImage(file="tomato.png")
# this stupid line above is what is needed to add an image to the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# below you can not enter the path of the image. it would make toooo much sense for that
# instead you have to do something stupid which is the above
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label()
timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
timer_label.grid(column=1, row=0)

check_label = Label()
check_label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)








window.mainloop()

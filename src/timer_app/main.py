from tkinter import *
from timer_app.time_logic import CountdownTimer

timer = CountdownTimer(30)
SIZE = 420
MARGIN = 20

def tick():
    remaining = timer.remaining_time()
    hours = remaining // 60 //60
    minutes = remaining // 60 % 60
    seconds = remaining % 60
    labelTime.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    if remaining >= 0:
        window.after(1000, tick)
    else:
      labelTime.config(text="Time's up!")

def clickStart():
    time = int(entry.get())
    timer.remaining = time
    tick()

def clickStop():
    global remaining
    remaining = 0

window = Tk()
window.title("tinyTimer")
window.geometry(f"{SIZE}x{SIZE}")
window.config(background="#3d3f41")
icon = PhotoImage(file="") # change to icon image file
# window.iconbitmap(True, icon)


myLabel = Label(window,
                text = "tinyTimer",
                font=("Arial", 40, "bold"),
                fg="white",
                bg="#3d3f41"
)
myLabel.pack()


labelTime = Label(window)
labelTime.config(text="00:00:00",
                font=("arial", 20),
                height=2,
                width=12,
)
labelTime.pack()

canvas_margin = 5
canvas_size = 150
canvasTime = Canvas(window, width=canvas_size, height=canvas_size)
canvasTime.create_arc(canvas_margin, canvas_margin, (canvas_size-canvas_margin), (canvas_size-canvas_margin), start=90, extent=-90, fill="red")
canvasTime.config(bg="#3d3f41",border=0, highlightthickness=0)
canvasTime.pack()

entry = Entry(window)
entry.config(font="arial",
            bg="#3d3f41",
            width=10,
)
entry.pack()


startBtn =  Button(window, text="Start")
startBtn.config(command=clickStart,
                bg="#363c46",
                activebackground="#3d3f41",
                fg="white",
                activeforeground="#3d3f41",
                compound="left"

)

startBtn.pack()


stopBtn = Button(window, text="Stop")
stopBtn.config(command=clickStop,
                bg="#363c46",
                activebackground="#3d3f41",
                fg="white",
                activeforeground="#3d3f41",
               compound="right"
)
stopBtn.pack()


window.mainloop()

from tkinter import *
from time_logic import *

timer = CountdownTimer(30)

def tick():
    remaining = next(timer.countdown())
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
window.geometry("420x300")
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

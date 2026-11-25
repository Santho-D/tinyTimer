from tkinter import Tk

from timer_app.time_logic import CountdownTimer
from timer_app.view import TimerView


def main():
    window = Tk()
    timer = CountdownTimer(30)
    TimerView(window, timer)
    window.mainloop()


if __name__ == "__main__":
    main()

from tkinter import Button, Canvas, Entry, Label

from timer_app.state import State
from timer_app.time_logic import CountdownTimer


class TimerView:
    SIZE = 420

    def __init__(self, window, timer: CountdownTimer):
        self.window = window
        self.timer = timer
        self.total_duration = timer.remaining

        self.window.title("tinyTimer")
        self.window.geometry(f"{self.SIZE}x{self.SIZE}")
        self.window.config(background="#3d3f41")

        self.title_label = Label(
            self.window,
            text="tinyTimer",
            font=("Arial", 40, "bold"),
            fg="white",
            bg="#3d3f41",
        )
        self.title_label.pack()

        self.time_label = Label(self.window)
        self.time_label.config(
            text="00:00:00",
            font=("arial", 20),
            height=2,
            width=12,
        )
        self.time_label.pack()

        canvas_margin = 5
        canvas_size = 150
        self.time_canvas = Canvas(
            self.window,
            width=canvas_size,
            height=canvas_size,
        )
        self.arc_id = self.time_canvas.create_arc(
            canvas_margin,
            canvas_margin,
            canvas_size - canvas_margin,
            canvas_size - canvas_margin,
            start=90,
            extent=-360,
            fill="red",
        )
        self.time_canvas.config(
            bg="#3d3f41",
            border=0,
            highlightthickness=0,
        )
        self.time_canvas.pack()

        self.entry = Entry(self.window)
        self.entry.config(
            font="arial",
            bg="#3d3f41",
            width=10,
        )
        self.entry.pack()

        self.start_button = Button(self.window, text="Start")
        self.start_button.config(
            command=self.click_start,
            bg="#363c46",
            activebackground="#3d3f41",
            fg="white",
            activeforeground="#3d3f41",
            compound="left",
        )
        self.start_button.pack()

        self.stop_button = Button(self.window, text="Stop")
        self.stop_button.config(
            command=self.click_stop,
            bg="#363c46",
            activebackground="#3d3f41",
            fg="white",
            activeforeground="#3d3f41",
            compound="right",
        )
        self.stop_button.pack()

        self.reset_button = Button(self.window, text="Reset")
        self.reset_button.config(
            command=self.click_reset,
            bg="#363c46",
            activebackground="#3d3f41",
            fg="white",
            activeforeground="#3d3f41",
        )
        self.reset_button.pack()

    def refresh(self):
        remaining = self.timer.remaining_time()
        fraction = (
            max(0, min(1, remaining / self.total_duration))
            if self.total_duration > 0
            else 0
        )
        self.time_canvas.itemconfig(self.arc_id, extent=-360 * fraction)
        total_seconds = int(remaining)
        hours = total_seconds // 3600
        minutes = total_seconds // 60 % 60
        seconds = total_seconds % 60
        self.time_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        return remaining

    def tick(self):
        remaining = self.refresh()
        if remaining > 0 and self.timer.state == State.RUNNING:
            self.window.after(1000, self.tick)
        elif remaining <= 0:
            self.time_label.config(text="Time's up!")

    def click_start(self):
        if self.timer.state == State.IDLE:
            self.total_duration = int(self.entry.get())
            self.timer.reset(self.total_duration)
            self.timer.start()
        if self.timer.state == State.PAUSED:
            self.timer.resume()
        self.tick()

    def click_stop(self):
        self.timer.pause()
        self.refresh()

    def click_reset(self):
        self.timer.reset(self.total_duration)
        self.refresh()

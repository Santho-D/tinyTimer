import time

from src.state import State


class CountdownTimer:
    '''Conflicting States will be silently ignored'''



    def __init__(self, duration, clock = time.monotonic):
        self.state = State.IDLE
        self.clock = clock
        self.remaining = duration
        self.end_time = None

    def start(self):
        '''Starts the timer'''
        if self.state == State.IDLE:
            self.end_time = self.clock() + self.remaining
            self.state = State.RUNNING

    def pause(self):
        '''Pauses the timer'''
        if self.state == State.RUNNING:
            self.remaining = max(0, self.end_time - self.clock())
            self.state = State.PAUSED


    def resume(self):
        '''Resumes the timer after pause'''
        if self.state == State.PAUSED:
            self.end_time = self.clock() + self.remaining
            self.state = State.RUNNING


    def stop(self):
        '''Ends the timer'''
        if self.state == State.RUNNING or self.state == State.PAUSED:
            self.state = State.FINISHED
            self.remaining = 0
            self.end_time = None

    def remaining_time(self):
        '''Returns remaining time'''
        if self.end_time != None:
            if self.state == State.PAUSED:
                return self.remaining
            else:
                self.remaining = max(0, self.end_time - self.clock())
                return self.remaining
        else:
            return self.remaining

    def is_finished(self):
        '''Reports when timer has ended'''
        if self.remaining_time() <= 0:
            self.state = State.FINISHED
        return self.state

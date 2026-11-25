from src.state import State
from src.time_logic import CountdownTimer

class FakeClock:
    def __init__(self, seconds=0):
        self.time = seconds
    def advance(self, seconds):
        self.time += seconds

def test_timer_is_idle():
    timer = CountdownTimer(60)
    assert timer.state == State.IDLE

def test_timer_is_running():
    timer = CountdownTimer(60)
    timer.start()
    assert timer.state == State.RUNNING

def test_timer_is_paused():
    timer = CountdownTimer(60)
    timer.start()
    timer.pause()
    assert timer.state == State.PAUSED

def test_timer_is_stopped():
    timer = CountdownTimer(60)
    timer.start()
    timer.stop()
    assert timer.state == State.FINISHED


def test_timer_is_finished():
    clock = FakeClock(2)
    timer = CountdownTimer(clock.time)
    timer.start()
    clock.advance(2)
    assert timer.is_finished() == State.FINISHED

def test_remaining_time_on_idle_timer():
    timer = CountdownTimer(60)
    assert timer.remaining_time() == 60

def test_stopped_timer_stays_frozen():
    clock = FakeClock(2)
    timer = CountdownTimer(clock.time)
    timer.start()
    timer.stop()
    first = timer.remaining_time()
    clock.advance(2)
    assert timer.remaining_time() == first

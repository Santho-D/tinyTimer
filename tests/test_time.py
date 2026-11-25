from timer_app.state import State
from timer_app.time_logic import CountdownTimer


class FakeClock:
    def __init__(self, now=0):
        self.now = now

    def __call__(self):
        return self.now

    def advance(self, seconds):
        self.now += seconds


def create_timer(duration=60, start_time=0):
    clock = FakeClock(start_time)
    return CountdownTimer(duration, clock=clock), clock


def test_timer_is_idle():
    timer, _ = create_timer()
    assert timer.state == State.IDLE


def test_timer_is_running():
    timer, _ = create_timer()
    timer.start()
    assert timer.state == State.RUNNING


def test_timer_is_paused():
    timer, _ = create_timer()
    timer.start()
    timer.pause()
    assert timer.state == State.PAUSED


def test_timer_is_endped():
    timer, _ = create_timer()
    timer.start()
    timer.end()
    assert timer.state == State.FINISHED


def test_timer_is_finished():
    timer, clock = create_timer(duration=2)
    timer.start()
    clock.advance(2)
    assert timer.is_finished() == State.FINISHED


def test_remaining_time_on_idle_timer():
    timer, _ = create_timer()
    assert timer.remaining_time() == 60


def test_paused_timer_stays_frozen():
    timer, clock = create_timer(duration=10)
    timer.start()
    clock.advance(3)
    timer.pause()
    first = timer.remaining_time()
    clock.advance(4)
    assert timer.remaining_time() == first


def test_resume_paused_timer():
    timer, clock = create_timer(duration=10)
    timer.start()
    clock.advance(3)
    timer.pause()

    assert timer.remaining_time() == 7

    clock.advance(4)
    assert timer.remaining_time() == 7

    timer.resume()
    assert timer.state == State.RUNNING
    clock.advance(2)
    assert timer.remaining_time() == 5

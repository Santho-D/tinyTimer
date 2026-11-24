from asyncio.base_futures import _FINISHED

import pytest
from modules.time_logic import CountdownTimer, State
import time


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
    timer = CountdownTimer(1)
    timer.start()
    time.sleep(2)
    assert timer.is_finished() == State.FINISHED

def test_remaining_time_on_idle_timer():
    timer = CountdownTimer(60)
    assert timer.remaining_time() == 60

def test_stopped_timer_stays_frozen():
    timer = CountdownTimer(5)
    timer.start()
    timer.stop()
    first = timer.remaining_time()
    time.sleep(1)
    assert timer.remaining_time() == first

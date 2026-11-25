from timer_app.view import TimerView


class FakeTimer:
    def __init__(self, remaining):
        self.remaining = remaining

    def remaining_time(self):
        return self.remaining


class FakeCanvas:
    def __init__(self):
        self.updated_item = None
        self.updated_options = None

    def itemconfig(self, item, **options):
        self.updated_item = item
        self.updated_options = options


class FakeLabel:
    def __init__(self):
        self.options = None

    def config(self, **options):
        self.options = options


def test_refresh_updates_arc_from_remaining_time():
    view = TimerView.__new__(TimerView)
    view.timer = FakeTimer(15)
    view.total_duration = 30
    view.arc_id = 1
    view.time_canvas = FakeCanvas()
    view.time_label = FakeLabel()

    view.refresh()

    assert view.time_canvas.updated_item == 1
    assert view.time_canvas.updated_options == {"extent": -180}
    assert view.time_label.options == {"text": "00:00:15"}

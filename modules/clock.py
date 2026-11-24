def countdown(remaining):
    while remaining > 0:
        yield remaining
        remaining -= 1

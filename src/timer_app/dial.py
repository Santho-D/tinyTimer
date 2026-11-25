class Dial:
    def __init__(self, max_minutes=60):
        if max_minutes <= 0 :
            raise ValueError
        self.max_minutes = max_minutes

    def minutes_to_fraction(self, minutes):
        '''Returns a fractional value (0-1); Takes time in minutes '''
        fraction = max (0, min( 1, (minutes / self.max_minutes)))
        return fraction

class Glassware:
    def __init__(self):
        pass # does nothing
class Beaker(Glassware):
    def __init__(self):
        super().__init__()
class Tray:
    def __init__(self):
        self.beakers = [Beaker() for _ in range(5)]
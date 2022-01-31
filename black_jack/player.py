class Player:
    count = 0

    def __init__(self, name):
        self.name = name
        self.status = None
        self.count += 1

    @property
    def set_status(self):
        return self.status

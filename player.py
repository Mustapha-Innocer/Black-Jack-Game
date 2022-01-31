class Player:
    count = 1

    def __init__(self, name, status):
        self.name = name
        self.status = status
        self.count += 1

    @property
    def set_status(self):
        return self.status

    @property
    def get_status(self):
        return self.status

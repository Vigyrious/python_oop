class Song:
    def __init__(self, name, length, is_single=bool):
        self.name = name
        self.length = float(length)
        self.is_single = is_single


    def get_info(self):
        return f"{self.name} - {self.length}"

    
class Logs:
    def __init__(self):
        self.entries = []

    def add_entry(self, message):
        self.entries.append(message)

    def get_entries(self):
        return self.entries
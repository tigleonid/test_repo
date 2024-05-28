class Logs:
    def __init__(self):
        self.entries = []

    def log(self, message):
        self.entries.append(message)
        print(f"Logged: {message}")

class Logs:
    def __init__(self):
        self.logs = []

    def add_log(self, message):
        self.logs.append(message)
        print(f'Log added: {message}')

    def display_logs(self):
        for log in self.logs:
            print(log)
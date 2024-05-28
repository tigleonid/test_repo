class Logs:
    def __init__(self, filename='default.log'):
        self.filename = filename
        
    def write_log(self, level, message):
        with open(self.filename, 'a') as file:
            file.write(f"{level}: {message}\n")
    
    def info(self, message):
        self.write_log('INFO', message)
    
    def error(self, message):
        self.write_log('ERROR', message)

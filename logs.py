class Logs:
    def __init__(self):
        # Initialize the logger
        self.logger = None

    def setup_logger(self, log_level):
        import logging
        # Create logger
        self.logger = logging.getLogger('ProjectLogger')
        self.this.logger.setLevel(log_level)
        
        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(log_level)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Add formatter to ch
        ch.setFormatter(formatter)

        # Add ch to logger
        self.logger.addHandler(ch)

    def log(self, level, message):
        if self.logger:
            getattr(self.logger, level)(message)
        else:
            print(f'Logger not set. Message: {message}')

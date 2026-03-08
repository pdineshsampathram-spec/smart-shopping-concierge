import datetime

class Logger:
    def log(self, component, message):
        timestamp = datetime.datetime.now().isoformat()
        print(f"[{timestamp}] [{component}] {message}")

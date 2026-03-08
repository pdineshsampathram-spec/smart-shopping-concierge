class SessionMemory:
    def __init__(self):
        self.history = []
        self.preferences = {}

    def add_message(self, message):
        self.history.append(message)

    def get_history(self):
        return self.history

    def set_preference(self, key, value):
        self.preferences[key] = value

    def get_preferences(self):
        return self.preferences

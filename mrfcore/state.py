class ReasoningState:
    def __init__(self, text: str):
        self.text = text
        self.log = []
        self.phase = "start"

        self.metrics = {}
        self.flags = {}
        self.history = []

    def finalize(self):
        return {
            "text": self.text,
            "log": self.log,
            "phase": self.phase,
            "metrics": self.metrics,
            "flags": self.flags,
            "history": self.history,
        }

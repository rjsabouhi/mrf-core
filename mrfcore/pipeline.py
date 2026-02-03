from .engine import MRFCoreEngine


class Pipeline:
    def __init__(self, operators):
        self.operators = operators

    def run(self, text: str):
        engine = MRFCoreEngine(enforce_phases=False)
        return engine.run_chain(self.operators, text)

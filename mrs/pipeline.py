from .engine import MRSCoreEngine

class ReasoningPipeline:
    def __init__(self, operators=None):
        self.operators = operators or []

    def run(self, text: str):
        engine = MRSCoreEngine(enforce_phases=False)
        return engine.run_chain(self.operators, text)

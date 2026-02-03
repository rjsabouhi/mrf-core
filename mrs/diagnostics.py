class MRSDiagnostics:
    """
    Lightweight diagnostics module for inspecting engine runs.
    """

    @staticmethod
    def summarize(result):
        return {
            "final_text": result.get("text"),
            "phase": result.get("phase"),
            "history": result.get("history", []),
            "log_entries": len(result.get("log", [])),
        }

    @staticmethod
    def show_log(result):
        return result.get("log", [])

    @staticmethod
    def count_violations(result):
        return sum(1 for entry in result.get("log", []) if "[VIOLATION]" in entry)

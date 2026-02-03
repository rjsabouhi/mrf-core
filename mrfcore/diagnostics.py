class MRFDiagnostics:
    """
    Lightweight diagnostics module for inspecting engine runs.
    """

    @staticmethod
    def summarize(result):
        """
        Produce a simple summary of the reasoning output.
        """
        return {
            "final_text": result.get("text"),
            "phase": result.get("phase"),
            "history": result.get("meta", {}).get("history", []),
            "log_entries": len(result.get("log", []))
        }

    @staticmethod
    def show_log(result):
        """
        Return the full operator log.
        """
        return result.get("log", [])

    @staticmethod
    def count_violations(result):
        """
        Count how many operator-phase violations occurred.
        """
        return sum(1 for entry in result.get("log", []) if "[VIOLATION]" in entry)

class MRFError(Exception):
    """Base class for all MRF-related errors."""
    pass


class OperatorNotFound(MRFError):
    """Raised when attempting to use an operator that has not been registered."""
    def __init__(self, operator_name):
        super().__init__(f"Operator not found: {operator_name}")
        self.operator_name = operator_name


class OperatorExecutionError(MRFError):
    """Raised when an operator raises an internal error."""
    def __init__(self, operator_name, original_exception):
        super().__init__(f"Operator '{operator_name}' failed: {original_exception}")
        self.operator_name = operator_name
        self.original_exception = original_exception


class InvalidPipelineConfig(MRFError):
    """Raised when a pipeline is incorrectly configured."""
    pass


class DiagnosticsWarning(MRFError):
    """Non-fatal diagnostic warning."""
    pass

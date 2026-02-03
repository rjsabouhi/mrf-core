class MRSError(Exception):
    """Base exception for MRS-Core."""
    pass


class OperatorNotFound(MRSError):
    pass


class MRSOperatorExecutionError(MRSError):
    pass


class MRSInvalidPipelineConfig(MRSError):
    pass

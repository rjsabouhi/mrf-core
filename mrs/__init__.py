"""
MRS-Core: Deterministic operator-based reasoning engine.
"""

from importlib.metadata import version as _version

# Safe version exposure
try:
    __version__ = _version("mrs-core")
except Exception:
    __version__ = "unknown"

from .engine import MRSCoreEngine
from .pipeline import ReasoningPipeline
from .state import ReasoningState
from .diagnostics import MRSDiagnostics
from .exceptions import (
    MRSError,
    OperatorNotFound,
    MRSOperatorExecutionError,
    MRSInvalidPipelineConfig,
)
from .presets import get_preset
from . import operators

__all__ = [
    "MRSCoreEngine",
    "ReasoningPipeline",
    "ReasoningState",
    "MRSDiagnostics",
    "MRSError",
    "OperatorNotFound",
    "MRSOperatorExecutionError",
    "MRSInvalidPipelineConfig",
    "get_preset",
    "operators",
]

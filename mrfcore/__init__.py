"""
MRF-Core
--------

A lightweight, modular, deterministic reasoning engine designed for
LLM autonomy, safety layers, and constraint-based reasoning.

This package exposes:
 - MRFCoreEngine (main executor)
 - Pipeline (operator runner wrapper)
 - ReasoningState (stateful reasoning object)
 - Diagnostics
 - Exceptions
 - Presets
"""

from .engine import MRFCoreEngine
from .pipeline import Pipeline
from .state import ReasoningState
from .diagnostics import MRFDiagnostics
from .exceptions import (
    MRFError,
    OperatorNotFound,
    OperatorExecutionError,
    InvalidPipelineConfig,
    DiagnosticsWarning,
)
from .presets import get_preset

__all__ = [
    "MRFCoreEngine",
    "Pipeline",
    "ReasoningState",
    "MRFDiagnostics",
    "MRFError",
    "OperatorNotFound",
    "OperatorExecutionError",
    "InvalidPipelineConfig",
    "DiagnosticsWarning",
    "get_preset",
]

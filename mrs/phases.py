# phases.py — MRS-Core
# Defines legal phase transitions and validation logic.

# Phase transition map for strict reasoning flow
PHASE_FLOW = {
    "start": "transform",
    "transform": "reflect",
    "reflect": "evaluate",
    "evaluate": "rewrite",
    "rewrite": "summarize",
    "summarize": "done",
    "done": "done",
}


def next_phase(operator_name, current_phase):
    """
    Given the current phase, return the next allowed phase.
    Engine.py requires this — do NOT remove.
    """
    return PHASE_FLOW.get(current_phase, "done")


# Legal phase definitions for each operator
LEGAL_PHASES = {
    "transform": ["start"],
    "reflect": ["transform"],
    "evaluate": ["reflect"],
    "rewrite": ["evaluate"],
    "summarize": ["rewrite"],
    # Inspect & filter are utility ops usable later in the chain
    "inspect": ["evaluate", "rewrite", "summarize"],
    "filter": ["evaluate", "rewrite", "summarize"],
}


def validate_phase(operator_name, current_phase):
    """
    Return an error string if operator is used in an illegal phase.
    Return None if legal.

    Engine.py expects:
        - None = OK
        - String = violation
    """
    allowed = LEGAL_PHASES.get(operator_name, [])
    if current_phase not in allowed:
        return f"Operator '{operator_name}' not allowed in phase '{current_phase}'"
    return None


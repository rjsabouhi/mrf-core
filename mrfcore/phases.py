PHASE_FLOW = {
    "start": "transform",
    "transform": "reflect",
    "reflect": "evaluate",
    "evaluate": "rewrite",
    "rewrite": "summarize",
    "summarize": "done",
    "done": "done",
}


def validate_phase(operator_name, current_phase):
    # permissive for now
    return None


def next_phase(operator_name, current_phase):
    return PHASE_FLOW.get(current_phase, "done")

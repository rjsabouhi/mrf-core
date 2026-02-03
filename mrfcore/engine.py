from .state import ReasoningState
from .registry import OperatorRegistry
from .phases import validate_phase, next_phase

# CRITICAL: forces operator registration
import mrfcore.operators  # noqa: F401


class MRFCoreEngine:
    def __init__(self, enforce_phases: bool = True):
        self.enforce_phases = enforce_phases

    def run_chain(self, operators, text: str):
        state = ReasoningState(text=text)

        for operator_name, params in operators:
            op_key = operator_name.lower()

            if self.enforce_phases:
                violation = validate_phase(op_key, state.phase)
                if violation:
                    state.log.append(f"[VIOLATION] {violation}")
                    continue

            operator_cls = OperatorRegistry.get(op_key)
            operator = operator_cls()

            state = operator(state, **params)

            state.history.append({
                "operator": op_key,
                "text": state.text,
                "phase": state.phase,
                "metrics": dict(state.metrics),
            })

            new_phase = next_phase(op_key, state.phase)
            if new_phase != state.phase:
                state.log.append(f"[PHASE] {state.phase} -> {new_phase}")
                state.phase = new_phase

        return state.finalize()

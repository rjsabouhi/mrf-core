from .base import BaseOperator
from ..registry import register_operator

@register_operator("evaluate")
class EvaluateOperator(BaseOperator):
    def __call__(self, state, **_):
        text = state.text
        state.text = f"{text}\n[EVAL chars={len(text)} words={len(text.split())}]"
        state.log.append("Evaluate applied")
        return state

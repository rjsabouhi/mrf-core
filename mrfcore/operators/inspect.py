from .base import BaseOperator
from ..registry import register_operator


@register_operator("inspect")
class InspectOperator(BaseOperator):
    def __call__(self, state, **_):
        state.log.append(f"Inspect len={len(state.text)}")
        return state

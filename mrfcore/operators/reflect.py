
from .base import BaseOperator
from ..registry import register_operator


@register_operator("reflect")
class ReflectOperator(BaseOperator):
    def __call__(self, state, **_):
        state.text = f"[REFLECT] {state.text}"
        state.log.append("Reflect applied")
        return state

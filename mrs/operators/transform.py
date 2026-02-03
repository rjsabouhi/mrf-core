from .base import BaseOperator
from ..registry import register_operator

@register_operator("transform")
class TransformOperator(BaseOperator):
    def __call__(self, state, instruction="expand", **_):
        if instruction == "expand":
            state.text = f"[TRANSFORM] {state.text}"
        state.log.append("Transform applied")
        return state

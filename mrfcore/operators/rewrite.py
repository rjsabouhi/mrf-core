from .base import BaseOperator
from ..registry import register_operator


@register_operator("rewrite")
class RewriteOperator(BaseOperator):
    def __call__(self, state, mode="upper", **_):
        state.text = state.text.upper() if mode == "upper" else state.text.lower()
        state.log.append("Rewrite applied")
        return state

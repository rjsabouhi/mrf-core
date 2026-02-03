from .base import BaseOperator
from ..registry import register_operator


@register_operator("filter")
class FilterOperator(BaseOperator):
    def __call__(self, state, word="", **_):
        if word:
            state.text = state.text.replace(word, "")
        state.log.append("Filter applied")
        return state

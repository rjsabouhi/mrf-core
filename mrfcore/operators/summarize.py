from .base import BaseOperator
from ..registry import register_operator


@register_operator("summarize")
class SummarizeOperator(BaseOperator):
    def __call__(self, state, max_words=5, **_):
        words = state.text.split()[:max_words]
        state.text = " ".join(words)
        state.log.append("Summarize applied")
        return state

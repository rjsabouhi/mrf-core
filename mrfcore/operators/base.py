from ..registry import register_operator


class BaseOperator:
    def __call__(self, state, **params):
        raise NotImplementedError

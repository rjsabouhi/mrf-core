class OperatorNotFound(Exception):
    pass


OPERATOR_REGISTRY = {}


def register_operator(name: str):
    key = name.lower()

    def decorator(cls):
        OPERATOR_REGISTRY[key] = cls
        return cls

    return decorator


class OperatorRegistry:
    @classmethod
    def get(cls, name: str):
        key = name.lower()
        if key not in OPERATOR_REGISTRY:
            raise OperatorNotFound(key)
        return OPERATOR_REGISTRY[key]

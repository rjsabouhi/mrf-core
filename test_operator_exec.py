from mrs.state import ReasoningState
from mrs.registry import OperatorRegistry

operators = [
    "transform",
    "reflect",
    "evaluate",
    "rewrite",
    "inspect",
    "filter",
    "summarize",
]

for op_name in operators:
    print(f"\n=== Testing {op_name.upper()} ===")
    op_cls = OperatorRegistry.get(op_name)
    op = op_cls()

    state = ReasoningState(text="Hello world. Testing operators.")
    result = op(state)
    print("Output text:", result.text)
    print("Log:", result.log[-1])

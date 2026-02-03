from mrfcore.registry import OPERATOR_REGISTRY

print("\n=== OPERATORS REGISTERED ===")
for name in sorted(OPERATOR_REGISTRY.keys()):
    print(" -", name)

print("\nTotal:", len(OPERATOR_REGISTRY))

from mrs.engine import MRSCoreEngine
from mrs.presets import get_preset

engine = MRSCoreEngine()
ops = get_preset("full_chain")

result = engine.run_chain(ops, "This is a test of the full chain preset.")

print("\nTEXT:", result["text"])
print("\nLOG:", result["log"])
print("\nPHASE:", result["phase"])
print("\nHISTORY LENGTH:", len(result["history"]))


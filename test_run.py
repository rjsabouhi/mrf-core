from mrs.engine import MRSCoreEngine
from mrs.presets import get_preset


def main():
    engine = MRSCoreEngine()
    operators = get_preset("reasoning")
    result = engine.run_chain(operators, "This is a test of MRS-Core.")

    print("\nFINAL TEXT:\n", result["text"])
    print("\nLOG:")
    for entry in result["log"]:
        print("-", entry)


if __name__ == "__main__":
    main()

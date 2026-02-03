from mrfcore.engine import MRFCoreEngine
from mrfcore.presets import get_preset


def main():
    engine = MRFCoreEngine()
    operators = get_preset("reasoning")
    result = engine.run_chain(operators, "This is a test of MRF-Core.")

    print("\nFINAL TEXT:\n", result["text"])
    print("\nLOG:")
    for entry in result["log"]:
        print("-", entry)


if __name__ == "__main__":
    main()

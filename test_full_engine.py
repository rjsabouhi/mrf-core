from mrs.engine import MRSCoreEngine
from mrs.presets import get_preset
from mrs.registry import OperatorRegistry


TEST_TEXT = """
MRS-Core is a modular deterministic reasoning pipeline.
We want to verify operator chaining, state transitions,
phase enforcement, and output determinism.
"""


def run_test(name, operators):
    print("\n============================")
    print(f"RUNNING TEST: {name}")
    print("============================")

    engine = MRSCoreEngine(enforce_phases=True)
    result = engine.run_chain(operators, TEST_TEXT)

    print("\nFINAL TEXT:")
    print(result["text"])

    print("\nPHASE:", result["phase"])

    print("\nLOG:")
    for entry in result["log"]:
        print("-", entry)

    print("\nHISTORY:")
    for h in result["history"]:
        print(h)


def test_presets():
    print("\n\n=== TEST: PRESETS ===")
    for preset_name in ["simple", "reasoning", "full_chain"]:
        operators = get_preset(preset_name)
        run_test(f"PRESET → {preset_name}", operators)


def test_random_chains():
    print("\n\n=== TEST: RANDOM ORDER CHAINS ===")

    ops = ["transform", "reflect", "evaluate", "rewrite",
           "inspect", "filter", "summarize"]

    chain = [
        ("transform", {}),
        ("rewrite", {"mode": "upper"}),
        ("evaluate", {}),
        ("summarize", {"max_words": 8}),
        ("reflect", {}),
    ]

    run_test("MANUAL RANDOM CHAIN", chain)


def test_invalid_operator():
    print("\n\n=== TEST: INVALID OPERATOR HANDLING ===")

    chain = [
        ("transform", {}),
        ("fake_operator", {}),  # should error
        ("summarize", {}),
    ]

    try:
        engine = MRSCoreEngine()
        engine.run_chain(chain, TEST_TEXT)
    except Exception as e:
        print("EXPECTED ERROR:", e)


def main():
    print("\n=== MRS-CORE FULL TEST SUITE ===\n")

    test_presets()
    test_random_chains()
    test_invalid_operator()

    print("\n=== ALL TESTS COMPLETED ===")


if __name__ == "__main__":
    main()

def get_preset(name: str):
    name = name.lower()

    presets = {
        "simple": [
            ("transform", {}),
            ("summarize", {}),
        ],
        "reasoning": [
            ("transform", {}),
            ("reflect", {}),
            ("evaluate", {}),
            ("rewrite", {}),
        ],
        "full_chain": [
            ("transform", {}),
            ("summarize", {}),
            ("reflect", {}),
            ("evaluate", {}),
            ("inspect", {}),
            ("filter", {}),
            ("rewrite", {}),
        ],
    }

    if name not in presets:
        raise ValueError(f"Unknown preset: {name}")

    return presets[name]

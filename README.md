# Modular Reasoning Framework (MRF-Core)
*A deterministic, operator-based reasoning engine for LLMs and autonomous agents.*

MRF-Core provides a transparent, modular, reproducible reasoning substrate built from a small set of reusable operators:

- Transform  
- Reflect  
- Evaluate  
- Rewrite  
- Summarize  
- Inspect  
- Filter  

MRF makes reasoning traceable, auditable, and deterministic—without requiring chain-of-thought exposure or hidden model internals.

---

# Why MRF-Core Exists

Every agent framework today suffers from the same structural failures:

## No consistent reasoning sequence  
## No deterministic backbone  
## No visibility into intermediate states  
## No enforceable phases or operator logic  

# MRF-Core solves this by introducing:

## Explicit operator-level reasoning  
## Strict phase transition model  
## Complete execution trace  
## Deterministic, reproducible outputs  
## Plug-and-play integration for ANY agent system  

MRF is **not** an alignment system.  
MRF is **not** a sandbox.  
MRF is a *reasoning substrate*.

---

# Features

## • Deterministic Reasoning Chains  
Operators execute in strict order.  
Output is repeatable.

## • Transparent Logs & History  
MRF records:  
- final text  
- operator log  
- phase trace  
- structured history of every step  

## • Simple, Extensible Operators  
Each operator is a small Python class registered via the Operator Registry.

## • Drop-In Presets  
`simple`, `reasoning`, `full_chain`  ready for production use.

---

# Install

```bash
pip install mrf-core
```

---


# Quick Start
from mrfcore.engine import MRFCoreEngine
from mrfcore.presets import get_preset

engine = MRFCoreEngine()
ops = get_preset("reasoning")

result = engine.run_chain(ops, "MRF-Core is a modular deterministic reasoning pipeline.")

```bash
print(result["text"])
print(result["log"])
print(result["phase"])
```
---

# Example Output
[REFLECT] [TRANSFORM]
MRF-CORE IS A MODULAR DETERMINISTIC REASONING PIPELINE.

[EVAL CHARS=95 WORDS=14]

PHASE: rewrite

---

# Running a Manual Operator Chain
from mrfcore.engine import MRFCoreEngine

engine = MRFCoreEngine()

ops = [
    ("transform", {}),
    ("reflect", {}),
    ("evaluate", {}),
    ("rewrite", {}),
]

result = engine.run_chain(ops, "Explain symbolic reasoning.")

print(result["text"])
print(result["history"])

---

# Using Presets

MRF-Core includes preset chains:
simple


reasoning


full_chain
from mrfcore.engine import MRFCoreEngine
from mrfcore.presets import get_preset

engine = MRFCoreEngine()

for name in ["simple", "reasoning", "full_chain"]:
    ops = get_preset(name)
    result = engine.run_chain(ops, "MRF-Core preset test")
    print(f"=== {name.upper()} ===")
    print(result["text"])

---

# Operator Anatomy
Every operator:
receives the current ReasoningState


modifies state.text


appends to state.log


updates state.phase


records an entry in state.history


Example:
@register_operator("reflect")
class ReflectOperator(Operator):
    phase = ("transform", "reflect")

    def run(self, state):
        state.text = f"[REFLECT] {state.text}"
        state.log.append("Reflect applied")
        return state

---

# Project Structure
mrfcore/
    engine.py
    registry.py
    state.py
    presets.py
    exceptions.py
    operators/
        base.py
        transform.py
        reflect.py
        evaluate.py
        rewrite.py
        summarize.py
        inspect.py
        filter.py
tests/
examples/

---

# What MRF-Core Is Not

MRF-Core is **NOT**:
- an alignment system  
- a safety guarantee  
- a sandbox  
- a replacement for secure execution layers  

MRF-Core **IS**:
- a deterministic reasoning layer  
- an operator execution engine  
- an audit-friendly cognition scaffold  
- a missing substrate for agent stability  

---

# Contributing

PRs welcome — especially new operators, presets, or diagnostics.

---

# License

Apache 2.0 — see LICENSE file.

Copyright 2026  
Ryan Sabouhi

---

# Notice

This software contains original work developed as part of the  
**Modular Reasoning Framework (MRF-Core)** by **Ryan Sabouhi**.  
See the `NOTICE` file for attribution details.

#
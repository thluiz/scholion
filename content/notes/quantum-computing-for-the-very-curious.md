---
title: "Quantum computing for the very curious"
date: '2020-07-05T14:10:32+00:00'
category: webclip
summary: 'The essay derives quantum computing from Turing and Deutsch, defines qubits as normalized complex vectors, then builds gates, measurement, CNOT, and the circuit model.'
tags: ["quantum-computing", "qubits", "quantum-gates", "measurement"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Quantum computing for the very curious"
    url: "https://quantum.country/qcvc"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/quantum-country--quantum-computing-for-the-very-curious.md"
    kind: repo
---

The essay starts from Turing’s and Deutsch’s questions about computation and physical systems, then frames quantum computers as devices that can efficiently simulate quantum mechanics. It argues that qubits are normalized vectors in a two-dimensional complex state space, and that quantum gates are unitary operations on those states.

## Reading notes

- Turing’s work on computability is presented as an attempt to formalize what an algorithm is, while Deutsch’s question shifts the basis to physical systems and efficient simulation.
- The essay claims computers are a fundamental feature of the universe and suggests alien civilizations would likely discover them as well.
- A qubit is defined as a unit-length vector in a two-dimensional complex vector space called state space.
- The computational basis states are |0⟩ and |1⟩, and general qubit states are superpositions with amplitudes.
- Measurement in the computational basis returns 0 or 1 with probabilities given by the squared moduli of the amplitudes, and it destroys the original amplitudes.
- The essay uses spaced-repetition testing as a mnemonic medium so readers can retain the material over long periods.
- The quantum NOT gate X swaps |0⟩ and |1⟩, acts linearly on superpositions, and is represented by a 2×2 matrix.
- Two X gates in sequence give back the original state, so the circuit is equivalent to a wire.
- The Hadamard gate maps |0⟩ and |1⟩ to equal superpositions with opposite signs, and H applied twice is the identity.
- Cancellation and reinforcement of amplitudes are presented as central ideas in quantum algorithms.
- A general single-qubit gate is represented by a 2×2 unitary matrix, and unitaries preserve vector length.
- The essay proves that a matrix preserves length if and only if it is unitary.
- The Pauli Y and Z gates are introduced as additional single-qubit gates.
- The CNOT gate acts on two qubits, flips the target when the control is 1, and can generate entangled states.
- The controlled-NOT is shown to be reversible, and the Toffoli gate is introduced as a three-qubit gate that can simulate classical AND.
- A general quantum computation is described as starting in a computational basis state, applying single-qubit and CNOT gates, and then measuring in the computational basis.
- Global phase factors do not affect measurement outcomes.
- The essay argues that the most important long-term use of quantum computers may be simulating quantum systems, especially for chemistry and materials science.
- Shor’s factoring algorithm is presented as the best-known example of a quantum speedup with major implications for encryption.
- The question of whether quantum computers can efficiently simulate every physical system remains open, especially for quantum gravity and general relativity.

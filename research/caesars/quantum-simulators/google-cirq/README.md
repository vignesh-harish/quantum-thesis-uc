# Google Cirq Quantum Simulator - Caesar Cipher Attack

This implementation uses Google's Cirq quantum computing framework to perform quantum-enhanced cryptanalysis on Caesar cipher encrypted texts.

## Quantum Simulator Details

- **Platform**: Google Quantum AI (Cirq)
- **Simulator**: cirq.Simulator
- **Quantum Algorithm**: Superposition-based search with measurement optimization
- **Qubits Used**: 5 LineQubits (representing 32 possible states, covering 0-25 shift values)

## Installation

```bash
pip install cirq
```

## Usage

```bash
python dec-caesars-cirq.py
```

## How It Works

1. **Qubit Creation**: Creates 5 LineQubits in a linear topology
2. **Superposition**: Applies Hadamard gates to create equal superposition
3. **Measurement**: Performs quantum measurements to sample shift candidates
4. **Frequency Analysis**: Uses measurement frequency to prioritize shift testing
5. **Classical Verification**: Tests shifts in quantum-guided order
6. **Decryption**: Uses found shift to decrypt all ciphertext files

## Quantum Advantages

- **Parallel Exploration**: Quantum superposition explores multiple states simultaneously
- **Measurement-Guided Search**: Quantum measurement statistics optimize classical search
- **Scalable Architecture**: LineQubit topology supports scalable quantum circuits
- **High-Fidelity Simulation**: Cirq provides accurate quantum state evolution

## Output

The script generates `decryption_metrics_cirq.txt` containing:
- Total attack time
- Quantum overhead measurements
- Per-file decryption metrics
- Quantum circuit statistics
- Measurement frequency analysis

## Cirq-Specific Features

- **LineQubits**: Linear qubit arrangement for straightforward circuit design
- **Circuit Composition**: Modular circuit construction with append operations
- **Flexible Measurement**: Named measurement keys for result tracking
- **Efficient Simulation**: Optimized state vector simulation

## Notes

- This is a simulator implementation demonstrating quantum computing principles
- Quantum overhead includes circuit creation, gate operations, and measurements
- Measurement results provide probabilistic guidance for classical verification
- Compatible with Google's quantum hardware architecture
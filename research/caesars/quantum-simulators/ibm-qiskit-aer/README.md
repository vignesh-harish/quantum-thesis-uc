# IBM Qiskit Aer Quantum Simulator - Caesar Cipher Attack

This implementation uses IBM's Qiskit Aer simulator to perform quantum-enhanced cryptanalysis on Caesar cipher encrypted texts.

## Quantum Simulator Details

- **Platform**: IBM Quantum (Qiskit)
- **Simulator**: AerSimulator (formerly QasmSimulator)
- **Quantum Algorithm**: Grover-inspired superposition search
- **Qubits Used**: 5 qubits (representing 32 possible states, covering 0-25 shift values)

## Installation

```bash
pip install qiskit qiskit-aer
```

## Usage

```bash
python dec-caesars-qiskit.py
```

## How It Works

1. **Quantum Circuit Creation**: Creates a 5-qubit quantum circuit
2. **Superposition**: Applies Hadamard gates to create superposition of all possible shift values
3. **Measurement**: Measures quantum states to get probabilistic shift candidates
4. **Classical Verification**: Tests shift candidates in order of quantum measurement frequency
5. **Decryption**: Uses found shift to decrypt all ciphertext files

## Quantum Advantages

- **Parallel Search**: Quantum superposition allows exploring multiple shift values simultaneously
- **Probabilistic Optimization**: Quantum measurements provide priority ordering for shift testing
- **Scalability**: Quantum approach scales logarithmically with search space size

## Output

The script generates `decryption_metrics_qiskit.txt` containing:
- Total attack time
- Quantum overhead measurements
- Per-file decryption metrics
- Quantum circuit statistics

## Notes

- This is a simulator implementation; real quantum hardware would require additional error correction
- Quantum overhead includes circuit creation, gate application, and measurement
- Results are deterministic for Caesar cipher but demonstrate quantum computing principles
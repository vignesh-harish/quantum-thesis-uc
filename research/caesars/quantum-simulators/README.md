# Quantum Simulators for Caesar Cipher Cryptanalysis

This directory contains implementations of quantum-enhanced Caesar cipher attacks using four major quantum computing simulators.

## Overview

Each subdirectory contains a complete implementation using a different quantum computing platform:

1. **IBM Qiskit Aer** - IBM's quantum computing framework
2. **Google Cirq** - Google's quantum programming framework
3. **Amazon Braket SDK** - AWS quantum computing service
4. **NVIDIA cuQuantum** - GPU-accelerated quantum simulation

## Directory Structure

```
quantum-simulators/
├── ibm-qiskit-aer/
│   ├── dec-caesars-qiskit.py
│   └── README.md
├── google-cirq/
│   ├── dec-caesars-cirq.py
│   └── README.md
├── amazon-braket/
│   ├── dec-caesars-braket.py
│   └── README.md
├── nvidia-cuquantum/
│   ├── dec-caesars-cuquantum.py
│   └── README.md
└── README.md (this file)
```

## Quantum Approach

All implementations use a similar quantum algorithm:

1. **Superposition Creation**: Apply Hadamard gates to create superposition of all possible shift values (0-25)
2. **Quantum Measurement**: Sample from the quantum state to get shift candidates
3. **Frequency Analysis**: Use measurement statistics to prioritize shift testing
4. **Classical Verification**: Test shifts in quantum-guided order
5. **Decryption**: Apply found shift to decrypt all ciphertext files

## Platform Comparison

| Platform | Simulator Type | Key Features | Hardware |
|----------|---------------|--------------|----------|
| **IBM Qiskit Aer** | State vector | Industry standard, extensive documentation | CPU |
| **Google Cirq** | State vector | Clean API, Google hardware compatible | CPU |
| **Amazon Braket** | State vector (SV1) | AWS integration, cloud-ready | CPU/Cloud |
| **NVIDIA cuQuantum** | Tensor network | GPU acceleration, high performance | GPU/CPU |

## Installation

### IBM Qiskit Aer
```bash
pip install qiskit qiskit-aer
```

### Google Cirq
```bash
pip install cirq
```

### Amazon Braket SDK
```bash
pip install amazon-braket-sdk
```

### NVIDIA cuQuantum
```bash
pip install cuquantum-python  # Requires NVIDIA GPU with CUDA
```

## Usage

Each implementation can be run independently:

```bash
# IBM Qiskit Aer
cd ibm-qiskit-aer
python dec-caesars-qiskit.py

# Google Cirq
cd google-cirq
python dec-caesars-cirq.py

# Amazon Braket
cd amazon-braket
python dec-caesars-braket.py

# NVIDIA cuQuantum
cd nvidia-cuquantum
python dec-caesars-cuquantum.py
```

## Output Files

Each implementation generates a metrics file:
- `decryption_metrics_qiskit.txt` (IBM Qiskit Aer)
- `decryption_metrics_cirq.txt` (Google Cirq)
- `decryption_metrics_braket.txt` (Amazon Braket)
- `decryption_metrics_cuquantum.txt` (NVIDIA cuQuantum)

## Metrics Collected

All implementations track:
- Total attack time (key discovery)
- Total decryption time
- Quantum overhead (circuit creation and execution)
- Per-file processing times
- Shift value found
- Success/failure status

## Quantum Advantages

While Caesar cipher is simple, these implementations demonstrate:
- **Parallel Search**: Quantum superposition explores multiple solutions simultaneously
- **Measurement-Guided Optimization**: Quantum statistics guide classical search
- **Scalability**: Quantum approach scales logarithmically with search space
- **Framework Comparison**: Shows differences between quantum platforms

## Performance Considerations

- **IBM Qiskit Aer**: Mature, well-documented, good for learning
- **Google Cirq**: Clean API, efficient for small circuits
- **Amazon Braket**: Cloud-ready, can scale to real quantum hardware
- **NVIDIA cuQuantum**: Fastest with GPU, best for large-scale simulations

## Real Quantum Hardware

These implementations are designed for simulators but can be adapted for real quantum hardware:
- **IBM Quantum**: Via IBM Quantum Experience
- **Google Quantum AI**: Via Google Cloud
- **Amazon Braket**: Via AWS quantum devices (IonQ, Rigetti, etc.)
- **NVIDIA**: Integration with quantum hardware partners

## Educational Value

These implementations demonstrate:
- Quantum circuit design
- Quantum measurement and sampling
- Hybrid quantum-classical algorithms
- Platform-specific quantum programming
- Performance comparison across simulators

## Limitations

- Caesar cipher is too simple to show true quantum advantage
- Simulators have overhead that real quantum hardware wouldn't have
- Small qubit count (5 qubits) doesn't showcase quantum scaling
- Classical verification still required for this problem

## Future Extensions

Possible enhancements:
- Implement Grover's algorithm for unstructured search
- Add quantum error correction
- Scale to more complex ciphers
- Benchmark against real quantum hardware
- Add quantum circuit optimization

## References

- IBM Qiskit: https://qiskit.org/
- Google Cirq: https://quantumai.google/cirq
- Amazon Braket: https://aws.amazon.com/braket/
- NVIDIA cuQuantum: https://developer.nvidia.com/cuquantum-sdk

## Notes

- All implementations include fallback mechanisms for missing dependencies
- Quantum overhead is estimated based on circuit complexity
- Results are deterministic for Caesar cipher but demonstrate quantum principles
- Each platform has unique strengths for different use cases
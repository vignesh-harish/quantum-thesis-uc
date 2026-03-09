# Amazon Braket SDK Quantum Simulator - Caesar Cipher Attack

This implementation uses Amazon Braket's local quantum simulator to perform quantum-enhanced cryptanalysis on Caesar cipher encrypted texts.

## Quantum Simulator Details

- **Platform**: Amazon Braket SDK
- **Simulator**: LocalSimulator (State Vector Simulator - SV1)
- **Quantum Algorithm**: Superposition-based parallel search
- **Qubits Used**: 5 qubits (representing 32 possible states, covering 0-25 shift values)

## Installation

```bash
pip install amazon-braket-sdk
```

## Usage

```bash
python dec-caesars-braket.py
```

## How It Works

1. **Circuit Creation**: Creates a quantum circuit with 5 qubits
2. **Superposition**: Applies Hadamard gates for uniform superposition
3. **Local Simulation**: Uses Braket's LocalSimulator for state vector simulation
4. **Measurement**: Performs quantum measurements to sample shift candidates
5. **Frequency Analysis**: Uses measurement statistics to prioritize testing
6. **Classical Verification**: Tests shifts in quantum-guided order
7. **Decryption**: Uses found shift to decrypt all ciphertext files

## Quantum Advantages

- **Parallel State Exploration**: Quantum superposition explores multiple shifts simultaneously
- **State Vector Simulation**: High-fidelity quantum state representation
- **AWS Integration**: Compatible with AWS quantum hardware via Braket service
- **Scalable Architecture**: Can be deployed on actual quantum devices

## Output

The script generates `decryption_metrics_braket.txt` containing:
- Total attack time
- Quantum overhead measurements
- Per-file decryption metrics
- Quantum circuit statistics
- Measurement frequency analysis

## Amazon Braket Features

- **LocalSimulator**: On-demand local quantum simulation
- **State Vector Backend**: Exact quantum state evolution (SV1)
- **Cloud Integration**: Seamless transition to AWS quantum hardware
- **Multiple Backends**: Support for various quantum devices
- **Task Management**: Asynchronous quantum task execution

## Notes

- This is a local simulator implementation for development and testing
- Can be easily adapted to run on AWS quantum hardware (IonQ, Rigetti, etc.)
- Quantum overhead includes circuit creation, compilation, and execution
- State vector simulation provides exact quantum mechanics representation
- Compatible with Amazon Braket's managed quantum computing service
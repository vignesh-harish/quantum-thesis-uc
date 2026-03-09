# NVIDIA cuQuantum - Caesar Cipher Attack

This implementation uses NVIDIA's cuQuantum SDK for GPU-accelerated quantum simulation to perform quantum-enhanced cryptanalysis on Caesar cipher encrypted texts.

## Quantum Simulator Details

- **Platform**: NVIDIA cuQuantum
- **Simulator**: GPU-accelerated tensor network simulator
- **Quantum Algorithm**: Tensor network contraction with GPU acceleration
- **Qubits Used**: 5 qubits (representing 32 possible states, covering 0-25 shift values)
- **Hardware**: NVIDIA GPU with CUDA support (falls back to CPU if unavailable)

## Installation

### With GPU Support (Recommended)
```bash
pip install cuquantum-python
# Requires NVIDIA GPU with CUDA 11.x or 12.x
```

### CPU Fallback
The script automatically falls back to CPU-based simulation if cuQuantum is not available.

## Usage

```bash
python dec-caesars-cuquantum.py
```

## How It Works

1. **State Initialization**: Creates initial quantum state |00000>
2. **Hadamard Application**: Applies Hadamard gates using tensor operations
3. **GPU Acceleration**: Uses NVIDIA GPU for tensor network contraction
4. **State Evolution**: Computes quantum state evolution on GPU
5. **Measurement Simulation**: Samples from probability distribution
6. **Classical Verification**: Tests shifts in quantum-guided order
7. **Decryption**: Uses found shift to decrypt all ciphertext files

## Quantum Advantages

- **GPU Acceleration**: Massive parallelization on NVIDIA GPUs
- **Tensor Network Optimization**: Efficient quantum state representation
- **Scalable Performance**: Handles larger quantum circuits efficiently
- **High Throughput**: Fast quantum state evolution and measurement

## Output

The script generates `decryption_metrics_cuquantum.txt` containing:
- Total attack time
- Quantum overhead measurements
- GPU acceleration statistics
- Per-file decryption metrics
- Performance comparisons

## NVIDIA cuQuantum Features

- **GPU-Accelerated Simulation**: Leverages CUDA cores for quantum operations
- **Tensor Network Contraction**: Optimized algorithms for state evolution
- **Memory Efficiency**: Smart memory management for large quantum states
- **Multi-GPU Support**: Can scale across multiple GPUs
- **High Performance**: Orders of magnitude faster than CPU simulation

## Hardware Requirements

### Optimal Performance
- NVIDIA GPU (Tesla, RTX, A100, H100, etc.)
- CUDA 11.x or 12.x
- 8GB+ GPU memory recommended

### Minimum Requirements
- CPU fallback mode (no GPU required)
- Standard Python environment

## Performance Notes

- GPU acceleration provides significant speedup for quantum simulations
- Tensor network methods are more efficient than state vector for certain circuits
- Performance scales with GPU compute capability
- Automatic fallback ensures compatibility without GPU

## Notes

- This implementation demonstrates GPU-accelerated quantum computing
- cuQuantum is optimized for NVIDIA GPUs but has CPU fallback
- Tensor network approach is memory-efficient for quantum circuits
- Compatible with NVIDIA's quantum computing ecosystem
- Can be integrated with other quantum frameworks (Qiskit, Cirq)
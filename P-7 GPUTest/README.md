# GPU Training Setup & Usage Guide

This guide explains how to set up and test GPU usage on a Lenovo IdeaPad Gaming 3 with an **NVIDIA GeForce GTX 1650** running Windows 11. It includes installation steps, verification, stress testing, and GPU memory management.

---

## 1. Check CUDA Version

Run this in **Command Prompt**:

```bash
nvidia-smi
```

Example output:

```cmd
Driver Version: 529.04       CUDA Version: 12.0
```

This confirms the system supports **CUDA 12.0**.

---

## 2. Install PyTorch with CUDA Support

Install PyTorch (with CUDA 12.1 support, compatible with CUDA 12.0 drivers):

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

---

## 3. Verify GPU in PyTorch

Run the following script:

```python
import torch

print("CUDA Available:", torch.cuda.is_available())
print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")
print("PyTorch CUDA Version:", torch.version.cuda)
print("Current Device:", torch.cuda.current_device())
```

Expected output:

```cmd
CUDA Available: True
GPU Name: NVIDIA GeForce GTX 1650
PyTorch CUDA Version: 12.1
Current Device: 0
```

---

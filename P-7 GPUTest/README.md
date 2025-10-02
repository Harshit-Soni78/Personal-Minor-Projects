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

## 4. Simple Training Test (GPU Check)

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Select device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using:", device)

# Dummy data
x = torch.randn(500, 10).to(device)
y = torch.randn(500, 1).to(device)

# Model
model = nn.Sequential(
    nn.Linear(10, 64),
    nn.ReLU(),
    nn.Linear(64, 1)
).to(device)

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training loop
for epoch in range(5):
    optimizer.zero_grad()
    outputs = model(x)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}/5, Loss: {loss.item():.4f}")
```

---

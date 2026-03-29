# HardLinux

**HardLinux — Your System Health Doctor** is a Python tool that monitors and reports your system’s health in real-time. It covers memory, swap, CPU, network, and disk usage, and provides a **health score** along with recommendations to optimize system performance.

---

## Features

- Memory (RAM) usage with human-readable units
- Swap memory monitoring
- CPU model, usage, and load analysis
- Network data usage (sent/received bytes)
- Disk usage monitoring
- Health score calculation
- Actionable recommendations for system optimization

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ISSELz/HardLinux.git
cd HardLinux
```
2. (Optional) Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
3. Install required packages:
```bash
pip install psutil
```

---

## Usage

- Run the main program:
```bash
python3 main.py
```
*You will see memory, swap, CPU, network, disk usage, and a system health score with actionable recommendations.

---

## Folder Structure

```bash
HardLinux/
├─ main.py
├─ README.md
├─ .gitignore
└─ hardlinux/
   ├─ __init__.py
   ├─ cpu.py
   ├─ memory.py
   ├─ swap.py
   ├─ network.py
   ├─ disk.py
   └─ __pycache__/
```

---

## Contributing

- Feel free to fork the project, improve features, or add new system checks. Submit pull requests with clear explanations of your changes.

---

## License

- This project is under the MIT License, which allows anyone to use, copy, modify, merge, publish, and distribute the code freely, while giving credit to the original author. It’s simple, permissive, and ideal for open-source projects like HardLinux.

---

## Notes

- Designed primarily for Linux systems; some features may not work on Windows or macOS.
- The health score is a simple metric based on resource usage percentages.
- Recommendations are general; always validate before taking critical system actions.

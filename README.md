# Network IDS – Enterprise-Grade Raspberry Pi + Arduino Intrusion Detection

Real-time Snort-based intrusion detection system for Raspberry Pi, with hardware alerts via Arduino.  
Detects scans, exploits, and unauthorized activity — then reacts using a buzzer, LED, or LCD.

---

## Features

- **Deep packet inspection with Snort**
- **Python-based log monitor and alert system**
- **Threat categorization via SID → alert type**
- **Arduino-controlled LED and buzzer for physical alerts**
- **Logs in `.log` and `.csv` (SIEM-ready)**
- **Auto-start using systemd**
- **Fully documented architecture, deployment, and wiring**

---

## Documentation

- **[System Architecture](docs/architecture.md)** – How it works end to end  
- **[Deployment Guide](docs/deployment.md)** – Setup instructions, Snort + systemd  

### Wiring Diagram  
![Wiring Diagram](docs/wiring_diagram.png)

### Demo  
![Demo](docs/demo.gif)

---

## Quick Start

### 1. Install Snort + Python Tools

```bash
sudo apt update
sudo apt install snort python3-pip nmap
pip3 install pyserial
```

### 2. Upload Arduino Code
Upload `arduino/alert_system.ino` to your Arduino (use pins 8 for LED, 9 for buzzer).

### 3. Enable Auto-Start (systemd)

```bash
sudo cp system/network-ids.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl enable network-ids
sudo systemctl start network-ids
```

---

## File Structure

```
network-ids-enterprise/
├── arduino/           # alert_system.ino
├── pi/                # monitor.py, sigmap.json
├── docs/              # architecture.md, deployment.md, diagrams
├── logs/              # Sample logs
├── system/            # systemd service
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Alert Types

| Alert Type    | Trigger SID | Arduino Response       |
|---------------|-------------|------------------------|
| UNAUTHORIZED  | Manual check| 1kHz buzz              |
| SCAN          | 1000001     | 2kHz sustained tone    |
| EXPLOIT       | 1000002     | 3x 3kHz beeps          |

---

## Use Cases

- Security+ / OSCP / CEH certification labs
- Raspberry Pi cybersecurity projects
- SOC simulation and training
- CTF home environment setup
- DIY network security appliance

---

## License

MIT License – See [LICENSE](LICENSE)

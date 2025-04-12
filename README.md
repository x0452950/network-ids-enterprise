# Network IDS – Enterprise-Grade Raspberry Pi + Arduino Intrusion Detection System

**Real-time intrusion detection using Snort on a Raspberry Pi, with Arduino-powered hardware alerting.**  
This system monitors network activity, detects suspicious traffic using Snort, and triggers audio/visual alerts via Arduino for real-world response and testing.

---

## Features

- **Snort-based deep packet inspection**
- **Threat categorization via SID mapping** (`sigmap.json`)
- **Logs alerts to `.log` and `.csv`** (SIEM/ELK friendly)
- **Hardware alerts via Arduino (buzzer + LED)** with tone-based threat types
- **Modular and portable design**
- **Runs on boot with `systemd` service**
- **Fully documented deployment + wiring + architecture**

---

## System Architecture

```
           [ Internet ]
                |
           [ Router / LAN ]
                |
         ┌──────────────────────┐
         │  Raspberry Pi (IDS)  │
         │ - Snort + Python     │
         │ - Log Monitor        │
         └──────────────────────┘
                  |
           USB Serial
                  |
         ┌──────────────────────┐
         │   Arduino Alert Box  │
         │ - LED + Buzzer       │
         │ - Future: LCD screen │
         └──────────────────────┘
```

---

## Setup

### 1. Install Dependencies

```bash
sudo apt update
sudo apt install python3-pip snort nmap
pip3 install pyserial
```

### 2. Add Custom Snort Rules

Edit `/etc/snort/rules/local.rules` and add:

```snort
alert tcp any any -> any 80 (msg:"Nmap Scan Detected"; flags:S; sid:1000001; rev:1;)
alert tcp any any -> any 443 (msg:"Exploit Attempt"; sid:1000002; rev:1;)
```

Restart Snort after saving.

### 3. Upload Arduino Code

Upload `arduino/alert_system.ino` using the Arduino IDE. Connect LED to pin 8 and buzzer to pin 9.

### 4. Enable the Systemd Service

```bash
sudo cp system/network-ids.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl enable network-ids.service
sudo systemctl start network-ids.service
```

---

## File Structure

```
network-ids/
├── arduino/           # Arduino sketch
├── pi/                # Python monitor, sigmap
├── logs/              # Sample alert logs
├── Docs/              # Diagrams, deployment, architecture
├── system/            # systemd service file
├── LICENSE            # MIT License
├── requirements.txt   # Python deps
└── README.md
```

---

## Alert Types

| Threat Type | Source SID   | Arduino Signal           |
|-------------|--------------|--------------------------|
| SCAN        | 1000001      | 2kHz tone (3 sec)        |
| EXPLOIT     | 1000002      | 3 short 3kHz beeps       |
| UNAUTHORIZED| Manual (ARP) | 1kHz tone (2 sec)        |

---

## Real Use Case

This project simulates an active SOC (Security Operations Center) environment in a lab.  
It’s great for:
- Cybersecurity certifications (Security+, OSCP)
- Raspberry Pi projects
- Teaching network defense
- CTF setups
- Home network threat detection

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

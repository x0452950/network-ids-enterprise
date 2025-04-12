# Deployment Guide

## Requirements
- Raspberry Pi OS
- Python 3
- `pyserial`, `nmap`, `snort`

## Steps

### 1. Install Dependencies
```bash
sudo apt update
sudo apt install python3-pip snort nmap
pip3 install pyserial
```

### 2. Set Up as a Service
```bash
sudo cp system/network-ids.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl enable network-ids.service
sudo systemctl start network-ids.service
```

### 3. Snort Rules
Make sure your `/etc/snort/rules/local.rules` has custom rule SIDs like:
```
alert tcp any any -> any 80 (msg:"Nmap Scan Detected"; flags:S; sid:1000001; rev:1;)
```

### 4. Logs
- Plain text: `ids_alert_log.txt`
- CSV (SIEM-ready): `ids_alert_log.csv`

# Raspberry Pi + Arduino Network IDS (Cert-Level)

This is an upgraded version of the original DIY alert system, now capable of real-time unauthorized device detection, nmap scanning, logging, and alert classification using a Raspberry Pi and Arduino.

## Features
- Detects unknown devices using `arp -a`
- Runs an `nmap -sn` scan for additional insight
- Sends different alerts to Arduino (UNAUTHORIZED vs SCAN)
- Logs all events with timestamps
- Uses buzzer tones and LED for alert types

## Usage
1. Set your known IPs in `AUTHORIZED_IPS`
2. Upload `alert_system.ino` to the Arduino
3. Connect Arduino via USB to the Pi
4. Run `monitor.py` on the Pi

## Requirements
- Python 3
- `pyserial`
- `nmap`

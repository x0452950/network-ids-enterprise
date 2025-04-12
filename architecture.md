# System Architecture

## Flow
1. Raspberry Pi runs `monitor.py`
2. Scans network using `arp -a` and `nmap`
3. Compares detected IPs to authorized list
4. Logs the event with timestamp
5. Sends alert via Serial to Arduino
6. Arduino responds with visual + audio signal

## Hardware
- Raspberry Pi 3 A+
- Arduino Uno
- LED + Resistor (Pin 8)
- Buzzer (Pin 9)

import serial
import time
import os
import json
import csv
from datetime import datetime

SNORT_LOG = "/var/log/snort/alert"
SIGNATURE_MAP = "sigmap.json"
ARDUINO_PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600
LOG_FILE = "ids_alert_log.txt"
CSV_FILE = "ids_alert_log.csv"

def log_event(message, threat="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {message}\n")
    with open(CSV_FILE, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, threat, message])
    print(f"[{timestamp}] {threat}: {message}")

def load_signature_map():
    if not os.path.exists(SIGNATURE_MAP):
        return {}
    with open(SIGNATURE_MAP, "r") as f:
        return json.load(f)

def parse_snort_log(sigmap):
    if not os.path.exists(SNORT_LOG):
        log_event("Snort log not found.")
        return "NONE"
    with open(SNORT_LOG, "r") as f:
        lines = f.readlines()
    for line in reversed(lines):
        for sig_id, threat_type in sigmap.items():
            if f"sid:{sig_id}" in line:
                return threat_type
    return "NONE"

def send_alert(alert_type="ALERT"):
    try:
        with serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=2) as arduino:
            time.sleep(2)
            arduino.write(f"{alert_type}\n".encode())
            log_event(f"Sent alert to Arduino: {alert_type}", alert_type)
    except Exception as e:
        log_event(f"Serial error: {e}", "ERROR")

def main():
    sigmap = load_signature_map()
    threat = parse_snort_log(sigmap)
    if threat != "NONE":
        send_alert(threat)
    else:
        log_event("No active threats.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import time
import subprocess

LOG_FILE = "/var/log/auth.log"
OUTPUT_LOG = "/home/alam/potinho-de-mel/logs/potinho.log"  # logs de monitoramento


def monitor_log():
    print("🚨 Monitor Potinho iniciado...")
    with open(OUTPUT_LOG, "a") as out:
        try:
            proc = subprocess.Popen(["sudo", "tail", "-F", LOG_FILE], stdout=subprocess.PIPE, text=True)
            for line in proc.stdout:
                out.write(line)
                out.flush()
                if "Failed password" in line:
                    print(f"⚠️ Tentativa de login detectada: {line.strip()}")
        except KeyboardInterrupt:
            print("\nMonitor encerrado pelo usuário.")

if __name__ == "__main__":
    monitor_log()


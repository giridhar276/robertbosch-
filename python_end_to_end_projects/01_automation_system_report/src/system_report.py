import os
import sys
import csv
import platform
from pathlib import Path
import psutil

def collect_system_information():
    disk = psutil.disk_usage("/")
    memory = psutil.virtual_memory()

    return {
        "current_working_directory": os.getcwd(),
        "python_version": sys.version.split()[0],
        "operating_system": platform.system(),
        "platform": platform.platform(),
        "processor": platform.processor() or "Not available",
        "cpu_count_logical": psutil.cpu_count(logical=True),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_total_gb": round(memory.total / (1024 ** 3), 2),
        "memory_used_percent": memory.percent,
        "disk_total_gb": round(disk.total / (1024 ** 3), 2),
        "disk_used_percent": disk.percent,
    }

def save_report(data, report_file: Path):
    report_file.parent.mkdir(parents=True, exist_ok=True)
    with report_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Metric", "Value"])
        for key, value in data.items():
            writer.writerow([key, value])

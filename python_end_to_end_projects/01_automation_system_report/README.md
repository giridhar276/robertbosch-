# Automation Project: System Report and File Organizer

- `os` for folders and environment details
- `sys` for Python and platform information
- `shutil` for copying and moving files
- `psutil` for CPU, memory and disk information
- `logging` for application logs
- CSV report generation

## Project Flow

1. Create sample files.
2. Organize files by extension.
3. Copy the organized folder as a backup.
4. Collect system information.
5. Generate a CSV report.
6. Store execution details in a log file.

## Setup

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python main.py
```

## Output

- Organized files inside `output/organized_files`
- Backup inside `output/backup`
- System report inside `reports/system_report.csv`
- Logs inside `logs/automation.log`

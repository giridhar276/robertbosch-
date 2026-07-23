from src.file_organizer import create_sample_files, organize_files, create_backup
from src.system_report import collect_system_information, save_report
from src.logger_config import configure_logging
from pathlib import Path
import logging

def main():
    configure_logging()
    logging.info("Automation project started.")

    input_dir = Path("data/input")
    organized_dir = Path("output/organized_files")
    backup_dir = Path("output/backup")
    report_file = Path("reports/system_report.csv")

    create_sample_files(input_dir)
    organize_files(input_dir, organized_dir)
    create_backup(organized_dir, backup_dir)

    system_data = collect_system_information()
    save_report(system_data, report_file)

    logging.info("Automation project completed successfully.")
    print("Automation completed.")
    print(f"Organized files: {organized_dir}")
    print(f"Backup folder: {backup_dir}")
    print(f"System report: {report_file}")

if __name__ == "__main__":
    main()

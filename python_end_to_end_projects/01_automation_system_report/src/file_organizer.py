from pathlib import Path
import shutil
import logging

def create_sample_files(input_dir: Path):
    input_dir.mkdir(parents=True, exist_ok=True)
    sample_files = {
        "employee_report.txt": "Employee report sample",
        "sales.csv": "product,amount\nLaptop,75000\nMouse,1200",
        "settings.json": '{"theme": "light"}',
        "notes.txt": "Automation training notes",
        "logo.png": "sample image placeholder"
    }
    for filename, content in sample_files.items():
        file_path = input_dir / filename
        if not file_path.exists():
            file_path.write_text(content, encoding="utf-8")
            logging.info("Created sample file: %s", file_path)

def organize_files(input_dir: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)

    for file_path in input_dir.iterdir():
        if not file_path.is_file():
            continue

        extension = file_path.suffix.lower().replace(".", "") or "no_extension"
        destination_folder = output_dir / extension
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / file_path.name
        shutil.copy2(file_path, destination)
        logging.info("Copied %s to %s", file_path, destination)

def create_backup(source_dir: Path, backup_dir: Path):
    if backup_dir.exists():
        shutil.rmtree(backup_dir)
    shutil.copytree(source_dir, backup_dir)
    logging.info("Backup created at %s", backup_dir)

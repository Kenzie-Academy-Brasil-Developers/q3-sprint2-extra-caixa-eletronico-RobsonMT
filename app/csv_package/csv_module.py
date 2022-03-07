from pathlib import Path
import os

FILEPATH = os.getenv("FILEPATH")

def create_csv_file():
    csv_file = Path(FILEPATH)
    command = os.system(f"touch {FILEPATH}")
    if not csv_file.is_file(): 
        command
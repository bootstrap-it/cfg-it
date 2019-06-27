from pathlib import Path
import yaml

def config_file(file_path: Path):
    try:
        return yaml.safe_load(file_path.open())
    except FileNotFoundError:
        return {}
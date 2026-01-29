from dataclasses import dataclass
from datetime import datetime


VALID_LEVELS = {"INFO", "WARNING", "ERROR"}

@dataclass
class LogEntry:
    timestamp: str
    level: str
    message: str

def is_valid_timestamp(date_part, time_part):
    try:
        datetime.strptime(f"{date_part} {time_part}", "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False


def parse_line(line):
    parts = line.strip().split(" ", 3)

    if len(parts) < 4:
        return None

    date_part, time_part, level, message = parts

    if not is_valid_timestamp(date_part, time_part):
        return None
    
    if level not in VALID_LEVELS:
        return None

    timestamp = f"{date_part} {time_part}"
    return LogEntry(timestamp, level, message)

    
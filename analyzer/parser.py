from dataclasses import dataclass

@dataclass
class LogEntry:
    timestamp: str
    level: str
    message: str

def parse_line(line):
    parts = line.strip().split(" ", 3)

    if len(parts) < 4:
        return None
    
    timestamp = f"{parts[0]} {parts[1]}"
    level = parts[2]
    message = parts[3]

    return LogEntry(timestamp, level, message)

    
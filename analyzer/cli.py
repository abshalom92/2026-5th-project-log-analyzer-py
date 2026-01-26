from analyzer.parser import parse_line

def load_log_file(path):
    entries = []

    with open(path, "r") as file:
        for line in file:
            entry = parse_line(line)
            if entry:
                entries.append(entry)

    return entries
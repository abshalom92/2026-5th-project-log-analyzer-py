from datetime import datetime

def filter_by_date(entries, since=None, until=None):
    filtered = []

    for entry in entries:
        entry_date = datetime.strptime(entry.timestamp, "%Y-%m-%d %H:%M:%S")

        if since and entry_date <since:
            continue
        if until and entry_date > until:
            continue
        
        filtered.append(entry)

    return filtered
from collections import Counter

def count_levels(entries):
    return Counter(entry.level for entry in entries)

def most_common_errors(entries, limit=3):
    errors = [e.message for e in entries if e.level=="ERROR"]
    return Counter(errors).most_common(limit)
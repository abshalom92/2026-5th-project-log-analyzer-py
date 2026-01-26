from analyzer.cli import load_log_file
from analyzer.stats import count_levels, most_common_errors

def main():
    entries = load_log_file("sample.log")

    print(f"Total entries: {len(entries)}")

    levels = count_levels(entries)
    for level, count in levels.items():
        print(f"{level}: {count}")

    print("\nMost common errors:")
    for msg, count in most_common_errors(entries):
        print(f"{count}x - {msg}")

if __name__ == "__main__":
    main()
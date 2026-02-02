import argparse
from analyzer.cli import load_log_file
from analyzer.stats import count_levels, most_common_errors

def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze a log file and summarize its contents"
    )

    parser.add_argument(
        "logfile",
        help="Path to the log file"
    )

    parser.add_argument(
        "--top-errors",
        type=int,
        default=3,
        help="Number of most common errors to display (default:3)"
    )

    parser.add_argument(
        "--errors-only",
        action="store_true",
        help='Show only error statistics'
    )

    return parser.parse_args()



def main():
    args = parse_args()

    entries = load_log_file(args.logfile)

    print(f"Total entries: {len(entries)}")

    if not args.errors_only:
        levels = count_levels(entries)
        for level, count in levels.items():
            print(f"{level}: {count}")
    
    print("\nMost common errors:")
    for message, count in most_common_errors(entries, args.top_errors):
        print(f"{count}x - {message}")

if __name__ == "__main__":
    main()
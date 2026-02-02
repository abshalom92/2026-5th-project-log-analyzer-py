import argparse
import json
import csv
import sys
from analyzer.cli import load_log_file
from analyzer.stats import count_levels, most_common_errors
from analyzer.filter import filter_by_date
from datetime import datetime


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

    parser.add_argument(
        "--since",
        type=str,
        help="Start date (inclusive) in YYYY-MM-DD format"
    )    

    parser.add_argument(
        "--until",
        type=str,
        help="End date (inclusive) in YYYY-MM-DD format"
    )

    parser.add_argument(
        "--output",
        choices=["text", "json", "csv"],
        default="text",
        help="Output format (default: text)"
    )

    return parser.parse_args()



def main():
    args = parse_args()
    
    entries = load_log_file(args.logfile)

    since_date = datetime.strptime(args.since, "%Y-%m-%d") if args.since else None
    until_date = datetime.strptime(args.until, "%Y-%m-%d") if args.until else None

    entries = filter_by_date(entries, since=since_date, until=until_date)

    levels = count_levels(entries)
    top_errors = most_common_errors(entries, args.top_errors)

    results = {
        "total_entries": len(entries),
        "levels": dict(levels),
        "top_errors": [
            {"message": msg, "count": count}
            for msg, count in top_errors
        ]
    }

    if args.output == "text":
        print(f"Total entries: {results['total_entries']}")
        
        if not args.errors_only:
            for level, count in results["levels"].items():
                print(f"{level}: {count}")

        print("\nMost common errors:")
        for error in results["top_errors"]:
            print(f"{error['count']}x - {error['message']}")
        
    elif args.output == "json":
        print(json.dumps(results, indent=2))

    elif args.output == "csv":
        writer = csv.writer(sys.stdout)

        writer.writerow(["Metric", "Value"])
        writer.writerow(["Total Entries", results["total_entries"]])

        writer.writerow([])
        writer.writerow(["Level", "Count"])
        for level, count in results["levels"].items():
            writer.writerow([level, count])
        
        writer.writerow([])
        writer.writerow(["Error Message", "Count"])
        for error in results["top_errors"]:
            writer.writerow([error["message"], error["count"]])


if __name__ == "__main__":
    main()
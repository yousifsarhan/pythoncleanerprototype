import argparse
import pandas as pd
from cleaner import clean_dataframe

def main():
    parser = argparse.ArgumentParser(description="Simple Python Data Cleaner")
    parser.add_argument("--in", dest="input_path", required=True, help="Input CSV file")
    parser.add_argument("--out", dest="output_path", required=True, help="Output cleaned CSV file")
    parser.add_argument("--report", dest="report_path", default=None, help="Optional HTML report path")
    args = parser.parse_args()

    df = pd.read_csv(args.input_path)
    cleaned = clean_dataframe(df)
    cleaned.to_csv(args.output_path, index=False)
    print(f" Cleaned file saved to: {args.output_path}")

    if args.report_path:
        try:
            from ydata_profiling import ProfileReport
            profile = ProfileReport(cleaned, title="Data Cleaner Report", explorative=True)
            profile.to_file(args.report_path)
            print(f"📄 Report saved to: {args.report_path}")
        except Exception as e:
            print("⚠️ Could not generate report. Install ydata-profiling or check errors.")
            print(e)

if __name__ == "__main__":
    main()

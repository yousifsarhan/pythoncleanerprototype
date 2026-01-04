Python Data Cleaner

A lightweight command-line Python tool for cleaning CSV datasets and generating automated data profiling reports.
Designed for quick preprocessing, exploratory analysis, and portfolio demonstration.

---

 Features

* Removes duplicate rows
* Trims whitespace from column names and values
* Automatically detects and converts numeric columns
* Handles missing values:

  * Numeric columns → filled with median
  * Text columns → filled with `"Unknown"`
* Exports a cleaned CSV file
* Generates an optional interactive HTML profiling report

---

Project Structure

pythoncleanerprototype/
├── cleaner.py          # Core data cleaning logic
├── main.py             # CLI entry point
├── requirements.txt    # Dependencies
├── README.md
└── data/
    ├── sample.csv      # Example input dataset
    └── cleaned.csv     # Example output (generated)




 Requirements

* Python 3.9+
* pip


Installation

Clone the repository and set up a virtual environment:

bash
git clone https://github.com/yousifsarhan/pythoncleanerprototype.git
cd pythoncleanerprototype

python -m venv .venv
source .venv/bin/activate    Windows: .venv\Scripts\activate

pip install -r requirements.txt




Usage

Run the cleaner from the command line:

bash
python main.py --in data/sample.csv --out data/cleaned.csv --report data/report.html


 Arguments

* `--in` : Path to input CSV file
* `--out` : Path to save cleaned CSV file
* `--report`: Path to save HTML profiling report



Output

cleaned.csv
  A cleaned version of the original dataset

report.html
  An interactive HTML report containing:

  * Column summaries
  * Missing value analysis
  * Data distributions
  * Basic statistics

Open the report by double-clicking the file or opening it in a browser.


Technologies Used

* Python
* Pandas
* ydata-profiling



Use Cases

* Data preprocessing before analysis or modeling
* Quick inspection of unfamiliar datasets
* Automation of repetitive CSV cleaning tasks
* Demonstration of Python data handling skills



Notes

* This is a command-line tool, not a web application.
* The HTML report is generated automatically — no manual editing required.
* GitHub Pages is not used, as Python does not run in a static environment.


Author

Yousif Sarhan
Information Technology & Multimedia Systems
GitHub: [https://github.com/yousifsarhan](https://github.com/yousifsarhan)

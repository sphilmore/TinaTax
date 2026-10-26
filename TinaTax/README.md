# TinaTax Form Test Suite

Automated tests for the contact form on [tinataxresolution.com](https://www.tinataxresolution.com). Tests are driven by a simple CSV file — no coding required to add or change test cases.

---

## Setup (one time only)

1. Make sure Python is installed on your computer
2. Open a terminal in this folder and run:
   ```
   pip install -r requirements.txt
   ```

---

## How to add test cases

Open `data/form_data.csv` in Excel or any spreadsheet app. Each row is one test case.

| Column | What to put |
|--------|-------------|
| `name` | Full name to submit |
| `email` | Email address |
| `phone` | Phone number |
| `service` | Service type (wrap in quotes if it contains a comma) |
| `message` | Message to submit |
| `expected_status` | `200` for a valid submission |

**Example:**
```
name,email,phone,service,message,expected_status
Jane Smith,jane@example.com,2155551234,IRS notice or letter,I need help with a notice,200
```

---

## How to run the tests

**Easy way** — double-click `run_tests.bat`. It will run all tests and open the results in Excel automatically.

**From the terminal** — open a terminal in this folder and run:

```
python -m pytest tests/ -v --csv=results.csv
```

Results will be saved to `results.csv` in plain English — open it in Excel to review.

---

## Project structure

```
TinaTax/
├── clients/
│   ├── form_api.py       # handles form submission requests
│   └── page_api.py       # handles website availability check
├── data/
│   └── form_data.csv     # your test cases go here
├── tests/
│   ├── test_form.py      # runs the form submission tests
│   └── test_get_api.py   # checks the website is reachable
├── utils/
│   └── csv_reader.py     # reads the CSV file
├── conftest.py           # shared test setup
└── requirements.txt      # dependencies
```

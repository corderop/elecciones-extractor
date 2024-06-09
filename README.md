# 🏫 Elecciones extractor

Extract the elections results from the Goverment website. It automatically updloads the result into a Google Sheets spreadsheet.

## How to use

1. Install the requirements

```bash
poetry install --without dev
```

2. Create a `.env` file with the variables specified in the `.env.example` file:

```bash
ELECCIONES_USER=myusername
ELECCIONES_PASSWORD=mypassword

GSHEET_ID=sheet_id
```

3. Create a spreadsheet with three sheets with the following names:

```
AVANCES-RAW
RES-C-MUN-RAW
RES-S-MUN-RAW
```

4. Run the script

```bash
python src/main.py
```

## Development

1. Install pre-commit in your computer

```bash
pip install pre-commit
```

2. Install pre-commit hooks

```bash
pre-commit install
```

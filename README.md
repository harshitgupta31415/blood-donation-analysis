# Blood Donation Registry Analysis

Exploratory analysis of a 30,000+ row donor registry using Pandas, Matplotlib,
and Seaborn. The project turns donor-level records into blood-type summaries
and six reproducible charts for supply, eligibility, and retention questions.

## Questions explored

- Which blood types have the largest donor populations?
- How does donor eligibility vary by blood type?
- What proportion of donors return within six months?
- How common are regular donors in the registry?
- How do BMI distributions and donation propensity differ across groups?

This is an educational analysis, not medical advice or a clinical prediction
system.

## Run the analysis

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

python -m pip install -r requirements.txt
python pandas_project.py
```

Use another input or output location:

```bash
python pandas_project.py --csv path/to/donors.csv --output reports
```

The command writes:

- `blood-type-summary.csv` with aggregated metrics;
- six PNG charts for donor distribution, return behaviour, regular-donor
  status, BMI, six-month outcomes, and eligibility.

Generated files are ignored by Git so the repository stays focused on source
and reproducible inputs.

## Dataset

The included CSV is the machine-learning-ready Blood Donor Registry dataset
published on [Kaggle](https://www.kaggle.com/datasets/tarekmasryo/blood-donor-registry-dataset).
It includes donor demographics, donation history, eligibility, and a six-month
outcome field. Consult the source page for the dataset's provenance and usage
terms.

## Project structure

```text
.
├── blood_donation_registry_ml_ready.csv  # source dataset
├── pandas_project.py                     # validation, aggregation, charts
├── requirements.txt
└── tests/
    └── test_analysis.py
```

## Test

```bash
python -m unittest discover -s tests -v
```

The test suite uses a small synthetic dataset; it does not depend on the full
CSV.

## Repository hygiene

Virtual environments are machine-specific build artifacts and are intentionally
excluded. Recreate dependencies from `requirements.txt` instead of committing
`.venv/` or `venv/`.

## License

Code in this repository is available under the MIT License. The dataset retains
the terms published by its original provider.

# Contributing to Blood Donation Registry Analysis

Contributions may improve validation, reproducibility, visual clarity, or the questions explored by the analysis.

## Local checks

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

Use synthetic rows for automated tests instead of expanding the committed dataset. Every new chart should answer a documented question, have readable labels, and be produced deterministically by `pandas_project.py`. Treat results as descriptive analysis rather than medical advice or clinical prediction.

Pull requests that change an aggregate should explain the formula and include a regression test for missing or malformed data.

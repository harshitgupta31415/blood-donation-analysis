from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import pandas as pd

from pandas_project import build_summary, load_data, run_analysis


def sample_rows() -> list[dict[str, object]]:
    return [
        {
            "donor_id": 1,
            "blood_type": "A+",
            "bmi": 22.5,
            "donation_count_last_12m": 2,
            "is_regular_donor": 1,
            "eligible_to_donate": 1,
            "donation_propensity_score": 80.0,
            "donated_next_6m": 1,
        },
        {
            "donor_id": 2,
            "blood_type": "O-",
            "bmi": 24.0,
            "donation_count_last_12m": 0,
            "is_regular_donor": 0,
            "eligible_to_donate": 1,
            "donation_propensity_score": 30.0,
            "donated_next_6m": 0,
        },
    ]


class AnalysisTests(unittest.TestCase):
    def test_load_data_removes_duplicate_rows(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            pd.DataFrame(sample_rows() + [sample_rows()[0]]).to_csv(path, index=False)
            self.assertEqual(len(load_data(path)), 2)

    def test_build_summary_calculates_group_rates(self) -> None:
        summary = build_summary(pd.DataFrame(sample_rows()))
        a_positive = summary.loc[summary["blood_type"] == "A+"].iloc[0]
        self.assertEqual(a_positive["donor_count"], 1)
        self.assertEqual(a_positive["future_donation_rate"], 1.0)

    def test_run_analysis_writes_summary_and_six_charts(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "sample.csv"
            pd.DataFrame(sample_rows()).to_csv(source, index=False)
            _, written = run_analysis(source, root / "reports")
            self.assertEqual(len(written), 7)
            self.assertTrue(all(path.is_file() for path in written))


if __name__ == "__main__":
    unittest.main()

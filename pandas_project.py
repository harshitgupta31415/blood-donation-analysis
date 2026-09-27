"""Explore blood-donor behaviour and export a reproducible chart set."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


REQUIRED_COLUMNS = {
    "donor_id",
    "blood_type",
    "bmi",
    "donation_count_last_12m",
    "is_regular_donor",
    "eligible_to_donate",
    "donation_propensity_score",
    "donated_next_6m",
}


def load_data(csv_path: str | Path) -> pd.DataFrame:
    """Load, validate, and de-duplicate the donor dataset."""

    data = pd.read_csv(csv_path)
    missing = sorted(REQUIRED_COLUMNS - set(data.columns))
    if missing:
        raise ValueError(f"dataset is missing required columns: {', '.join(missing)}")
    return data.drop_duplicates().copy()


def build_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Aggregate planning metrics by blood type."""

    return (
        data.groupby("blood_type", dropna=False)
        .agg(
            donor_count=("donor_id", "count"),
            avg_bmi=("bmi", "mean"),
            avg_donations_12m=("donation_count_last_12m", "mean"),
            regular_donor_rate=("is_regular_donor", "mean"),
            eligibility_rate=("eligible_to_donate", "mean"),
            avg_propensity=("donation_propensity_score", "mean"),
            future_donation_rate=("donated_next_6m", "mean"),
        )
        .reset_index()
        .sort_values("blood_type")
    )


def create_figures(data: pd.DataFrame, summary: pd.DataFrame) -> dict[str, plt.Figure]:
    """Build the six figures used by the report."""

    sns.set_theme(style="whitegrid", context="notebook")
    figures: dict[str, plt.Figure] = {}

    figure, axis = plt.subplots(figsize=(10, 6))
    sns.barplot(data=summary, x="donor_count", y="blood_type", hue="blood_type", palette="viridis", legend=False, ax=axis)
    axis.set(title="Donor Distribution by Blood Type", xlabel="Number of Donors", ylabel="Blood Type")
    figures["01-donor-distribution"] = figure

    figure, axis = plt.subplots(figsize=(10, 6))
    sns.barplot(data=summary, x="future_donation_rate", y="blood_type", hue="blood_type", palette="coolwarm", legend=False, ax=axis)
    axis.set(title="Future Donation Likelihood by Blood Type", xlabel="Observed donation rate", ylabel="Blood Type", xlim=(0, 1))
    figures["02-future-donation-rate"] = figure

    figure, axis = plt.subplots(figsize=(8, 6))
    sns.countplot(data=data, x="is_regular_donor", hue="is_regular_donor", palette="Set2", legend=False, ax=axis)
    axis.set(title="Regular vs Non-Regular Donors", xlabel="Regular donor (0 = no, 1 = yes)", ylabel="Number of Donors")
    figures["03-regular-donors"] = figure

    figure, axis = plt.subplots(figsize=(12, 6))
    sns.violinplot(data=data, x="blood_type", y="bmi", hue="blood_type", palette="Set2", inner="quartile", legend=False, ax=axis)
    axis.set(title="BMI Distribution Across Blood Types", xlabel="Blood Type", ylabel="BMI")
    figures["04-bmi-distribution"] = figure

    donation_counts = data["donated_next_6m"].value_counts().reindex([0, 1], fill_value=0)
    figure, axis = plt.subplots(figsize=(7, 7))
    axis.pie(
        donation_counts.values,
        labels=["Did not donate", "Donated"],
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette("Set2", 2),
    )
    axis.set_title("Donation Outcome in the Next Six Months")
    figures["05-next-six-month-outcome"] = figure

    figure, axis = plt.subplots(figsize=(10, 6))
    sns.barplot(data=summary, x="eligibility_rate", y="blood_type", hue="blood_type", palette="magma", legend=False, ax=axis)
    axis.set(title="Eligibility Rate by Blood Type", xlabel="Eligibility rate", ylabel="Blood Type", xlim=(0, 1))
    figures["06-eligibility-rate"] = figure

    for figure in figures.values():
        figure.tight_layout()
    return figures


def run_analysis(csv_path: str | Path, output_dir: str | Path) -> tuple[pd.DataFrame, list[Path]]:
    """Run the analysis and write its reusable outputs."""

    data = load_data(csv_path)
    summary = build_summary(data)
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)

    summary_path = destination / "blood-type-summary.csv"
    summary.to_csv(summary_path, index=False)
    written = [summary_path]

    for name, figure in create_figures(data, summary).items():
        path = destination / f"{name}.png"
        figure.savefig(path, dpi=160, bbox_inches="tight")
        plt.close(figure)
        written.append(path)
    return summary, written


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        type=Path,
        default=Path(__file__).with_name("blood_donation_registry_ml_ready.csv"),
        help="source CSV file",
    )
    parser.add_argument("--output", type=Path, default=Path("reports"), help="directory for generated files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    summary, written = run_analysis(args.csv, args.output)
    print(f"Analysed {int(summary['donor_count'].sum()):,} de-duplicated donor records.")
    print(summary.to_string(index=False))
    print("\nGenerated:")
    for path in written:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



"""Run 10 training iterations with different settings, all logged to MLflow.

Usage: python -m src.run_experiments
Then: mlflow ui
"""

from src.config import load_params
from src.train import train_and_log

# Each experiment lists only the settings that change.
EXPERIMENTS = [
    # Original 3 experiments
    {"model": "random_forest", "n_estimators": 50, "max_depth": 4},
    {"model": "random_forest", "n_estimators": 100, "max_depth": 6},
    {"model": "random_forest", "n_estimators": 200, "max_depth": 8},

    # 7 additional experiments
    {"model": "random_forest", "n_estimators": 50, "max_depth": 12},
    {"model": "random_forest", "n_estimators": 100, "max_depth": 4},
    {"model": "random_forest", "n_estimators": 200, "max_depth": 6},
    {"model": "random_forest", "n_estimators": 300, "max_depth": 8},
    {"model": "random_forest", "n_estimators": 100, "min_samples_leaf": 10},
    {"model": "random_forest", "n_estimators": 200, "min_samples_leaf": 20},
    {"model": "random_forest", "n_estimators": 300, "min_samples_leaf": 1},
]


def main():
    base = load_params()["train"]

    print(f"Running {len(EXPERIMENTS)} experiments...")

    for i, changes in enumerate(EXPERIMENTS, start=1):
        # Merge the original training settings with this experiment's changes.
        settings = {**base, **changes}

        print(f"\nExperiment {i}/10: {settings}")

        train_and_log(
            settings,
            run_name=f"exp-{i:02d}"
        )

    print("Done. Run `mlflow ui` and compare the runs.")


if __name__ == "__main__":
    main()

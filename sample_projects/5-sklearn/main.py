from argparse import ArgumentParser
from json import dumps
from pathlib import Path
from typing import Literal

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from tqdm import tqdm

ModelName = Literal["logreg", "random_forest"]


def build_model(model_name: ModelName, seed: int):
    if model_name == "logreg":
        return LogisticRegression(max_iter=300, random_state=seed)
    return RandomForestClassifier(n_estimators=200, random_state=seed)


def run(model_name: ModelName, test_size: float, seed: int, out_dir: Path) -> Path:
    x, y = load_iris(return_X_y=True)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size, random_state=seed, stratify=y
    )

    model = build_model(model_name, seed)
    for _ in tqdm(range(1), desc="training", unit="step"):
        model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "report.json"
    payload = {
        "model": model_name,
        "test_size": test_size,
        "seed": seed,
        "accuracy": accuracy,
        "classification_report": report,
    }
    out_path.write_text(dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"model={model_name}")
    print(f"accuracy={accuracy:.4f}")
    print(f"saved={out_path.resolve()}")
    return out_path


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        "--model",
        choices=["logreg", "random_forest"],
        default="logreg",
        help="classifier type",
    )
    parser.add_argument("--test-size", type=float, default=0.2)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out-dir", type=Path, default=Path("output"))
    args = parser.parse_args()
    run(args.model, args.test_size, args.seed, args.out_dir)


if __name__ == "__main__":
    main()

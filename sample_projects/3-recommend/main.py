from argparse import ArgumentParser
from pathlib import Path
from typing import Literal

from tqdm import tqdm


def run(mode: Literal["train", "eval"], data_dir: Path, steps: int) -> None:
    for _ in tqdm(range(steps), desc=f"{mode}", unit="step"):
        pass
    print(f"mode={mode}")
    print(f"data_dir={data_dir.resolve()}")


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--mode", choices=["train", "eval"], default="train")
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--steps", type=int, default=20)
    args = parser.parse_args()
    run(args.mode, args.data_dir, args.steps)


if __name__ == "__main__":
    main()

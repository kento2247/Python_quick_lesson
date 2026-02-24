# 4. Pythonインストール（uv使用）

自身が作成したコードを確実に実行し，他者が再現できるようにするには，Python実行環境を安定して管理することが重要です．  
本章では，その基盤として `uv` を使った環境構築手順を扱います．

## 4-1. なぜuvを使うか

`uv` はPython環境とパッケージ管理を高速に行えるツールです．

使う理由:

- `pip` / `venv` 相当の作業を1つのツールで扱える
- 仮想環境の作成と依存関係のインストールが速い
- プロジェクトごとの環境を分離しやすく，再現性を保ちやすい

### 非推奨なPython環境管理例

このレッスンでは `uv` に統一して環境を管理するため，次は避ける:

- `conda` / `anaconda` を使った環境管理
  - `base` 環境やチャネル設定がグローバルに効きやすく，プロジェクト外まで影響して環境汚染が起きやすい
  - `uv` と混在すると依存解決器と環境管理単位が二重化し，再現手順が不安定になる
  - 非常に上級者向けな運用が必要で，初心者にはハードルが高く，一般的なケースでは必要とならない
- `pyenv` を前提にした運用
  - Python本体の切り替え（`pyenv`）とライブラリ管理（`pip`/`uv`）が別管理になり，運用が複雑になる
  - 環境再現時に「Pythonバージョン再現 + 依存再現」の2段階が必要で，手間が増える
  - Python本体のビルドが入るため，導入や初期セットアップが遅くなりやすい
- Windowsで Microsoft Store 版Python をそのまま使う
  - 実行パスやエイリアス挙動が一般的な配布形態と異なり，環境差分が出やすい
  - チームで共有される標準的な手順とズレやすく，他者コードを動かしにくい
- Google Colaboratory で `ipynb` だけで進める
  - ランタイムがセッション依存で，依存関係や実行状態の再現が難しい
  - コード差分管理・レビュー・分割設計がしにくく，保守性が下がる
  - ファイルベース開発を前提としたAI coding（自動編集・テスト・リファクタ）と相性が悪い

方針:

- 本講座では Python本体の導入後は `uv venv` と `uv run` に統一する
- 依存関係は `pyproject.toml` と `uv.lock` で管理し，環境再現手順を1本化する
- 既存で `conda` / `pyenv` 環境が入っていても，本レッスン用プロジェクトでは切り離して運用する
---

## 4-2. uvインストールと動作確認

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

ターミナルを再起動して動作確認:

```bash
uv --version
```

---

## 4-3. 仮想環境の作成と有効化

プロジェクトルートで実行:

```bash
uv init
uv venv --python 3.13
source .venv/bin/activate
```
- `--python` でPythonのバージョンを指定可能（本教材のサンプルは `>=3.13` を想定）


確認:

```bash
which python
python --version
```

補足:

- プロンプトの先頭に `(.venv)` が表示されれば有効化できている
- 作業終了時は `deactivate` で仮想環境を抜ける

---

## 4-4. パッケージのインストールと管理

基本:

```bash
uv add numpy
uv add pandas
uv add matplotlib
```
または，3つまとめて:
```bash
uv add numpy pandas matplotlib
```

バージョン固定例:

```bash
uv add "numpy==2.1.1"
```

インストール済み確認: 

```bash
uv pip list
```

パッケージの削除
```bash
uv remove numpy
```

### uvの挙動
- `uv init` でプロジェクトルートに `pyproject.toml` が作成される
- `uv venv` で仮想環境 `.venv/` が作成される
- `uv add` で依存関係が `pyproject.toml` に追加され，`uv.lock` が更新される
- `uv run` で仮想環境内でコマンドを実行できる．仮想環境が未作成の場合は自動で作成され，依存関係も自動でインストールされる
- `uv sync` で `pyproject.toml` と `uv.lock` をもとに環境を再現できる

---

## 4-5. `uv run` / `uv sync` の使い分け

最小ルール:

- 自分のPCで「とりあえず実行」: `uv run ...`
- 既存プロジェクトの依存を先に揃える: `uv sync`

例:

```bash
# ロックファイルに合わせて環境を再現
uv sync

# 仮想環境内で実行
uv run main.py
```

---

## 4-6. Pandasサンプルコードの実行

`sample_projects/1-pandas` に移動して実行:

```bash
cd sample_projects/1-pandas
uv run main.py
```

結果:

```bash
❯ uv run main.py
=== 元データ ===
      Name  Age      City  Salary
0    Alice   28     Tokyo  450000
1      Bob   35     Osaka  520000
2  Charlie   42     Kyoto  580000
3    Diana   31     Tokyo  490000
4      Eve   26  Yokohama  420000

=== 都市ごと集計 ===
       City  people  avg_age  avg_salary  max_salary
0     Kyoto       1     42.0      580000      580000
1     Osaka       1     35.0      520000      520000
2     Tokyo       2     29.5      470000      490000
3  Yokohama       1     26.0      420000      420000

=== 給与トップ3 ===
   Name  City  Salary
Charlie Kyoto  580000
    Bob Osaka  520000
  Diana Tokyo  490000
```
- `uv run` を使うことで，仮想環境が未作成でも自動で準備される
- 依存関係は `sample_projects/1-pandas/pyproject.toml` に定義される
---

## 4-7. numpyサンプルコードの実行

`sample_projects/2-numpy` に移動して実行:

```bash
cd sample_projects/2-numpy
uv run main.py
```

結果例:

```bash
❯ uv run main.py
=== 1次元配列 ===
x: [1. 2. 3. 4. 5.]
y: [10. 20. 30. 40. 50.]
x + y: [11. 22. 33. 44. 55.]
xの平均: 3.0
yの標準偏差: 14.142135623730951

=== 2次元配列 ===
A:
[[1. 2.]
 [3. 4.]]
B:
[[5. 6.]
 [7. 8.]]
A @ B:
[[19. 22.]
 [43. 50.]]
```

- `uv run` を使うことで，仮想環境が未作成でも自動で準備される
- 依存関係は `sample_projects/2-numpy/pyproject.toml` に定義される

## 4-8. 推奨ライブラリとコーディング

研究コード・業務コードのどちらでも，次の標準/定番ライブラリを優先して使う:

- `argparse`: コマンドライン引数を安全に扱う（`--input`, `--seed` など）
- `tqdm`: 学習・前処理ループの進捗表示を簡単に追加できる
- `pathlib.Path`: ファイル/ディレクトリ操作をOS差分を意識せず記述できる
- `typing.Literal`: 関数引数の取りうる値を明示し，保守性を上げる

最小例:

```python
from argparse import ArgumentParser
from pathlib import Path
from typing import Literal

from tqdm import tqdm


def run(mode: Literal["train", "eval"], data_dir: Path, steps: int) -> None:
    for _ in tqdm(range(steps), desc=f"{mode}"):
        pass
    print(f"mode={mode}")
    print(f"data_dir={data_dir.resolve()}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--mode", choices=["train", "eval"], default="train")
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--steps", type=int, default=20)
    args = parser.parse_args()
    run(args.mode, args.data_dir, args.steps)
```

同じ内容を `sample_projects/3-recommend` にサンプルとして配置しているので，実際に動かして確認できる:

```bash
cd sample_projects/3-recommend
uv run main.py --mode train --data-dir data --steps 20
```

- 依存関係は `sample_projects/3-recommend/pyproject.toml` に定義される

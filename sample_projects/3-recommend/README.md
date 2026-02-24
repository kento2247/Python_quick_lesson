# 3-recommend

`README_sections/04_python_uv.md` の「4-8. 推奨ライブラリとコーディング」を実際に動かして確認するためのサンプルです．

## 使うライブラリ

- `argparse`: コマンドライン引数の処理
- `pathlib.Path`: パス操作
- `typing.Literal`: 取りうる値の明示
- `tqdm`: 進捗表示

## 実行方法

```bash
uv run main.py --mode train --data-dir data --steps 20
```

## 実装ポイント

- `--mode` は `train` / `eval` に制限
- `--data-dir` は `Path` 型として受け取る
- ループ進捗を `tqdm` で表示する

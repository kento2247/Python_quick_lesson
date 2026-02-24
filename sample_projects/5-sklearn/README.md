# 5-sklearn

`README_sections/04_python_uv.md` の内容を使い，`uv` で環境を再現しながら機械学習コードを実行するサンプルです．

## 実行方法

```bash
cd sample_projects/5-sklearn
uv run main.py --model random_forest --test-size 0.2 --seed 42
```

## このサンプルで確認できること

- `argparse` でCLI引数を扱う
- `pathlib.Path` で出力ディレクトリを扱う
- `typing.Literal` でモデル名の候補を制限する
- `tqdm` で進捗表示を出す
- `scikit-learn` で分類モデルを学習し，評価結果をJSON保存する

## 出力

実行後に `output/report.json` が生成されます．

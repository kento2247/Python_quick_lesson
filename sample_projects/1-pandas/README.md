# 1-pandas

PandasでCSVを読み込み，集計・ソートする基本を確認するサンプルです．

## 実行方法

```bash
cd sample_projects/1-pandas
uv run main.py
```

## このサンプルで確認できること

- `pd.read_csv` によるCSV読み込み
- 列追加（`AgeGroup`, `Salary_k`）
- `groupby` + `agg` による都市別集計
- 給与上位3名の抽出と表示

## 入力データ

- `sample.csv`: 人物名・年齢・都市・給与のサンプルデータ

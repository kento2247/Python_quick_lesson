# 最終目標

- Linux環境で開発できる
- Git / GitHubを使える
- uvで仮想環境管理できる
- 機械学習コードを実行できる

## 5-1. 最終課題の到達イメージ

これまでの章（OS/CLI, Git/GitHub, VSCode, uv）を統合し，次の2つを完成させる:

1. `sample_projects/4-mypage`
   - HTML/CSS/JavaScriptで自己紹介ページを作る
   - GitHubで管理し，必要ならGitHub Pagesで公開する
2. `sample_projects/5-sklearn`
   - `uv` で依存関係を管理し，`scikit-learn` 分類器を実行する
   - 実行結果を `output/report.json` に保存する

### 例：4-mypage

### 例：5-sklearn

```bash
cd sample_projects/5-sklearn
uv run main.py --model random_forest --test-size 0.2 --seed 42
```

- `uv run` により，仮想環境と依存関係が必要に応じて自動準備される
- 結果は `sample_projects/5-sklearn/output/report.json` に保存される

## 5-4. チェックリスト

- `git clone` で他者環境に取得できる
- `code .` でVSCodeから編集できる
- `uv run` でPython実行環境を再現できる
- 生成物（Webページ/機械学習結果）をGitHubで共有できる
